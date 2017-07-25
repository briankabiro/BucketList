from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

buckets = {}
users = {}
global bucketCount
global userCount
global new_user
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
    def __init__(self, name,Id,items=[]):
        self.name = name
        self.items = items
        self.Id = Id
        count = 0

    def return_name(self):
        # print the name of the created user
        print(self.name)

    def add_item(self, item):
        self.items.append({"Id": count, "body": item})
        count += 1

    def update_item(self, Id, item):
        for i in self.items:
            if i['Id'] == Id:
                i['body'] = item

    def remove_item(self, Id):
        for i in self.items:
            if i['Id'] == Id:
                del i

class User(object):
    #create new user
    def __init__(self, name, password, Id):
        self.name = name
        self.password = password
        self.Id = Id
    def return_name(self):
        return self.name

    def __del__(self):
        return True



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
    global new_user
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data,form.password.data,userCount)
        userCount += 1
        users[new_user.name] = new_user
        return redirect(url_for('view'))
    return render_template("signup.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ return the login page"""
    global new_user
    form = LoginForm()
    if form.validate_on_submit():
        if new_user.name == form.username.data:
            if new_user.password == form.password.data:
                return redirect(url_for('view'))
        return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/view', methods=['GET', 'POST'])
def view():
    # return the view page
    global new_user
    if request.method == "GET":
        return render_template("view.html")
    else:
        global bucketCount
        global users
        global new_user
        data = request.form.to_dict()
        bucket = data['bucket']
        new_bucket = Bucket(bucket, bucketCount)
        bucketCount += 1
        print("these are the ",buckets)
        if new_user.name in buckets:
            buckets[new_user.name].append(new_bucket)
        else:
            buckets[new_user.name] = []
            buckets[new_user.name].append(new_bucket)
        return render_template('view.html',data=buckets[new_user.name],user=new_user.name)


@app.route('/bucket/<bucket_id>/add_item')
def add_item(data):
    # add item to bucket
    #buckets[new_user][bucket_id].append(item`)
    # item.id, item.body
    # add item with id and the body text
    global new_user
    for i in buckets:
        if i['Id'] == bucket_id:
            i.add_item(data)


@app.route('/bucket/<bucket_id>/remove_item')
def remove_item():
    # remove item from the bucket list
    for i in buckets:
        if i.Id == bucket_id:
            i.remove_item(data)


@app.route('/bucket/<bucket_id>/update_item')
def update_item():
    # update the item in a bucket list
    #get the id and the data
    for i in buckets[new_user.name]:
        if i.Id == bucket_id:
            i.update_item(data)


@app.route('/bucket/<bucket_id>' ,methods=['POST'])
def view_bucket(bucket_id):
    # view the bucket list
    if request.method == 'POST':
        global new_user
        for i in buckets[new_user.name]:
            if i.Id == bucket_id:
                print("this is i", i)
                
        print("this is the object I'm sending",bucket)   
    return render_template('bucket.html',data=bucket)


@app.route("/view/edit_bucket/<bucket_id>")
def edit_bucket(bucket_id):
    # logic to edit a bucket list
    if request.method == 'POST':
        title = request.form['new_title']
        redirect(url_for('view'))
    else:
        return render_template('edit_bucket.html')
    

@app.route("/view/delete_bucket/<bucket_id>", methods=['POST'])
def delete_bucket(bucket_id):
    # function that deletes a bucket list
    global new_user
    for i in buckets[new_user.name]:
        if i.Id == bucket_id:
            buckets[new_user.name].remove(i)
    return redirect(url_for('view'))


if __name__ == "__main__":
    app.run(debug=True)