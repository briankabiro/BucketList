from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
global new_bucket

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder="../static",
    template_folder='../templates')
app.config['SECRET_KEY'] = "secret_key"
Bootstrap(app)


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


class Bucketlist(object):
    """ the class for a bucket list"""
    def __init__(self, name, bucket=[]):
        self.name = name
        self.bucket = bucket

    def return_name(self):
        """ print the name of the bucket """
        print(self.name)

    def __del__(self):
        """ delete the created object """
        return True

    def add_item(self, item):
        """ add an item to the bucket """
        self.bucket.append({"Id": len(self.bucket), "body": item})

    def update_item(self, item_id, item):
        """ update an existing item in the bucket """
        for i in self.bucket:
            if i['Id'] == item_id:
                i['body'] = item

    def remove_item(self, item_id):
        """ remove an item from the bucket"""
        for i in self.bucket:
            if i['Id'] == item_id:
                del i


class User(object):
    #create new user
    def __init__(self, name="", password=""):
        self.name = name
        self.password = password

    def return_name(self):
        """  return the name of the user """
        return self.name

    def __del__(self):
        """ delete the created object """
        return True


global new_user
new_user = User()


@app.route('/')
def index():
    # return the home page
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """return the signup page"""
    form = RegisterForm()
    if form.validate_on_submit():
        new_user.name = form.username.data
        new_user.password = form.password.data
        return redirect(url_for('index'))
    return render_template("signup.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ return the login page"""
    form = LoginForm()
    print(new_user.name, new_user.password)
    if form.validate_on_submit():
        if new_user.name == form.username.data:
            if new_user.password == form.password.data:
                return redirect(url_for('view'))
        return redirect(url_for('login'))
    return render_template("login.html", form=form)


@app.route('/view', methods=['GET', 'POST'])
def view():
    """ return the view page """

    if request.method == 'POST':
        requestDict = request.form.to_dict()
        print(requestDict)
        if requestDict['method'] == 'create':
            # get name of bucketlist from input
            global new_bucket
            new_bucket = Bucketlist(requestDict['title'])
            print("new bucket created")
            text = requestDict['itemBody']
            new_bucket.add_item(text)
            return jsonify(new_bucket.bucket)

        elif requestDict['method'] == 'add':
            text = requestDict['data']
            new_bucket.add_item(text)
            return jsonify(new_bucket.bucket)

        elif requestDict['method'] == 'updateItem':
            new_bucket.update_item()

        elif requestDict['method'] == 'removeItem':
            # get the id of element in bucket list and delete it
            new_bucket.remove_item(requestDict['index'])
            print('item has been removed from bucket')
            return jsonify(new_bucket.bucket)

        elif requestDict['method'] == 'delete':
            # id is gotten from the data sent from the client
            new_bucket.__del__()
            return "successfully deleted"

        elif requestDict['method'] == 'logout':
            # return the bucket
            new_user.name = ""
            new_user.password = ""
            return redirect(url_for('index'))

    else:
        if new_user.name != "":
            return render_template('view.html', user=new_user.name)
        return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)