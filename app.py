import os
import sys
sys.path.append(os.getcwd())
from models.bucket import Bucket
from models.user import User
from flask import Flask, session, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from app.forms import LoginForm, RegisterForm

buckets = {}
users = []
global bucketCount
global userCount
userCount = 0
bucketCount = 0

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder="./static",
    template_folder='./templates')

app.config['SECRET_KEY'] = "secret_key"

Bootstrap(app)

@app.route('/')
def index():
    # return the home page
    return render_template("index.html")


@app.route('/signup', methods=['GET','POST'])
def signup():
    """return the signup page"""
    global userCount
    error = None
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data, form.password.data, userCount)
        userCount += 1
        users.append(new_user)
        session['username'] = new_user.name
        return redirect(url_for('view'))
    return render_template("signup.html", form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    """ return the login page"""
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        for user in users:
            if user.name == form.username.data:
                if user.password == form.password.data:
                    session['username'] = user.name
                    return redirect(url_for('view'))
            error = 'Invalid credentials'
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/view', methods=['GET'])
def view():
    # return the view page
    if 'username' in session:
        if session['username'] not in buckets:
            buckets[session['username']] = []
        return render_template(
            'view.html',
            data=buckets[session['username']],
            user=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/view/create_bucket', methods=['POST'])
def create_bucket():
    # create the bucket
    if session['username'] in buckets:
        global bucketCount
        data = request.form.to_dict()
        print("this is data", data)
        bucket = data['bucket']
        new_bucket = Bucket(bucket, bucketCount)
        bucketCount += 1
        buckets[session['username']].append(new_bucket)
        return redirect(url_for('view'))


@app.route('/bucket/<bucket_id>', methods=['GET', 'POST'])
def view_bucket(bucket_id):
    # view the bucket list
    bucket = [
        i for i in buckets[session['username']] if str(i.Id) == bucket_id
    ]
    bucket = bucket[0]
    return render_template('bucket.html', bucket=bucket)



@app.route("/bucket/edit_bucket/<bucket_id>", methods=['POST'])
def edit_bucket(bucket_id):
    # logic to edit a bucket list
    if request.method == 'POST':
        title = request.form['title']
        bucket = [
            i for i in buckets[session['username']] if str(i.Id) == bucket_id
        ]
        bucket = bucket[0]
        bucket.update_name(title)
        return redirect(url_for('view'))


@app.route("/bucket/delete_bucket/<bucket_id>", methods=['POST'])
def delete_bucket(bucket_id):
    # function that deletes a bucket list
    for i in buckets[session['username']]:
        if str(i.Id) == bucket_id:
            buckets[session['username']].remove(i)
            print("this is buckets after deleting", buckets)
    return redirect(url_for('view'))

@app.route('/bucket/<bucket_id>/add_item', methods=['POST'])
def add_item(bucket_id):
    # add item to bucket
    data = request.form.to_dict()
    item = data['item']
    bucket = [
        i for i in buckets[session['username']] if str(i.Id) == bucket_id
    ]
    bucket = bucket[0]
    bucket.add_item(item)
    return redirect('/bucket/' + bucket_id)


@app.route('/bucket/<bucket_id>/remove_item/<item_id>', methods=['POST'])
def remove_item(bucket_id, item_id):
    # remove item from the bucket list
    if request.method == 'POST':
        bucket = [
            i for i in buckets[session['username']] if str(i.Id) == bucket_id
        ]
        bucket = bucket[0]
        item = [i for i in bucket.items if str(i['Id']) == bucket_id] 
        bucket.remove_item(item_id)
        return redirect('/bucket/' + bucket_id)

@app.route('/bucket/<bucket_id>/edit_item/<item_id>', methods=['POST'])
def edit_item(bucket_id, item_id):
    # update the item in a bucket list
    if request.method == 'POST':
        data = request.form.to_dict()
        new_text = data['new_text']
        bucket = [
            i for i in buckets[session['username']] if str(i.Id) == bucket_id
        ]
        bucket = bucket[0]
        item = [i for i in bucket.items if str(i['Id']) == item_id]
        item = item[0]
        print('this is item', item)
        print('this is bucket',bucket)
        
        bucket.update_item(item_id, new_text)
        return redirect('/bucket/' + bucket_id)


@app.route('/logout',methods=['POST'])
def logout():
    # logout a user
    session.pop('username')
    flash('You have been logged out')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)