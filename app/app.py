from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
from models.User import User
from models.Bucket import Bucket
buckets = {}

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder="../static",
    template_folder='../templates')
app.config['SECRET_KEY'] = "secret_key"
Bootstrap(app)
'''
    create views for different actions
    install nosetests
    set counter for creating ids
    finish functions for 
'''


class LoginForm(FlaskForm):
    username = StringField(
        'Username', validators=[InputRequired(),
                                Length(min=1)])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                Length(min=1)])


class RegisterForm(FlaskForm):
    username = StringField(
        'Username', validators=[InputRequired(),
                                Length(min=1)])
    password = PasswordField(
        'Password', validators=[InputRequired(),
                                Length(min=1)])



global new_user
new_user = User()

@app.route('/')
def index():
    # return the home page
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # return the signup page
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(form.username.data,form.password.data)
        new_user.name = form.username.data
        new_user.password = form.password.data
        return redirect(url_for('view'))
    return render_template("signup.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # return the login page
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
    # return the view page
    return render_template("view.html")

@app.route('/view/<bucket_id>/add_item')
def add_item():
    # add item to bucket
    #buckets[new_user][bucket_id].append(item`)
    pass


@app.route('/view/<bucket_id>/remove_item')
def remove_item():
    # remove item from the bucket list
    pass

@app.route('/view/<bucket_id>/update_item')
def update_item():
    # update the item in a bucket list
    pass

@app.route("/view/create_bucket")
def create_bucket_list():
    # create a bucket list
    if method == "POST":
        title = request.method.title      
        new_bucket = Bucket(title)

        buckets[new_user].append(new_bucket)    

@app.route('/view/<bucket_id>')
def view_bucket():
    # view the bucket list
    return render_template('bucket.html')

@app.route("/view/edit_bucket/<bucket_id>")
def edit_bucket(bucket_id):
    # logic to edit a bucket list
    if request.method == 'POST':
        title = request.form['new_title']
    return render_template('/view/edit_bucket.html')


@app.route("/view/delete_bucket")
def delete_bucket_list(bucket_id):
    # function that deletes a bucket list
    pass

        
if __name__ == "__main__":
    app.run(debug=True)