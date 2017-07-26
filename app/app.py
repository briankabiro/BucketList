import os
import sys
sys.path.append(os.getcwd())

from flask import Flask, session, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

buckets = {}
users = []
global bucketCount
global userCount
userCount = 0
bucketCount = 0

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder="../static",
    template_folder='../templates')

app.config['SECRET_KEY'] = "secret_key"

Bootstrap(app)


class Bucket(object):
    def __init__(self, name, Id, items=[], count=0):
        self.name = name
        self.items = items
        self.Id = Id
        self.count = count

    def return_name(self):
        # print the name of the created user
        print(self.name)

    def update_name(self, new_title):
        print("this is the old title",self.name)
        self.name = new_title
        print("this is the new_title", self.name)

    def add_item(self, item):
        self.items.append({"Id": self.count, "body": item})
        self.count += 1

    def update_item(self, Id, item):
        for i in self.items:
            if i['Id'] == Id:
                i['body'] = item

    def remove_item(self, Id):
        for i in self.items:
            if i['Id'] == Id:
                self.items.remove(i)


class User(object):
    #create new user
    def __init__(self, name, password, Id):
        self.name = name
        self.password = password
        self.Id = Id

    def return_name(self):
        return self.name


'''
    create views for different actions
    install nosetests
    set counter for creating ids
    finish functions for
'''


class LoginForm(FlaskForm):
    """the class for the login form"""
    username = StringField(
        'Username', validators=[InputRequired(),
                                Length(min=1)])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                Length(min=1)])


class RegisterForm(FlaskForm):
    """the class for the sign up form"""
    username = StringField(
        'Username', validators=[InputRequired(),
                                Length(min=1)])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                Length(min=1)])


@app.route('/')
def index():
    # return the home page
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """return the signup page"""
    global userCount
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data, form.password.data, userCount)
        userCount += 1
        users.append(new_user)
        session['username'] = new_user.name
        return redirect(url_for('view'))
    return render_template("signup.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ return the login page"""
    form = LoginForm()
    if form.validate_on_submit():
        for user in users:
            if user.name == form.username.data:
                if user.password == form.password.data:
                    session['username'] = user.name
                    return redirect(url_for('view'))
            return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/view', methods=['GET'])
def view():
    # return the view page
    if session['username']:
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
    if session['username'] in buckets:
        global bucketCount
        data = request.form.to_dict()
        print("this is data", data)
        bucket = data['bucket']
        new_bucket = Bucket(bucket, bucketCount)
        bucketCount += 1
        buckets[session['username']].append(new_bucket)
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
    return render_template('bucket.html', bucket=bucket)


@app.route('/bucket/<bucket_id>/remove_item/<item_id>', methods=['POST'])
def remove_item(bucket_id, item_id):
    # remove item from the bucket list
    if request.method == 'POST':
        bucket = [
            i for i in buckets[session['username']] if str(i.Id) == bucket_id
        ]
        bucket = bucket[0]
        item = [i for i in bucket.items if str(i['Id']) == bucket_id]
        print("this is item", item)        
        bucket.remove_item(item_id)
        return redirect(url_for('bucket'))

@app.route('/bucket/<bucket_id>/edit_item/<item_id>')
def edit_item(bucket_id, item_id):
    # update the item in a bucket list
    #get the id and the data
    if request.method == 'POST':
        new_text = request.form('text')
        bucket = [
            i for i in buckets[session['username']] if str(i.Id) == bucket_id
        ]
        bucket = bucket[0]
        item = [i for i in bucket.items if str(i['Id']) == item_id]
        item = item[0]
        bucket.update_item(item_id, new_text)
        return render_template('bucket.html', bucket=bucket)


@app.route('/bucket/<bucket_id>', methods=['GET', 'POST'])
def view_bucket(bucket_id):
    # view the bucket list
    if request.method == 'POST':
        bucket = [
            i for i in buckets[session['username']] if str(i.Id) == bucket_id
        ]
        bucket = bucket[0]
        return render_template('bucket.html', bucket=bucket)
    else:
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


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)