from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length


app = Flask(__name__, static_url_path='/static', static_folder="../static", template_folder='../templates')
app.config['SECRET_KEY'] = "secret_key"
Bootstrap(app)

class LoginForm(FlaskForm):
	username = StringField('Username', validators= [InputRequired(), Length(min=1)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1)])

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1)])	

##write the todo capture data on submit, send it to backend create bucketlist,on press button send data
class Bucketlist(object):
	def __init__(self, name, Id=0, bucket={}):
		self.name = name
		self.Id = Id
		self.bucket = bucket 

	def return_name(self):
		return self.name

	def __del__(self):
		return True

	def add_item(self, item):
		if self.Id not in self.bucket:
			self.bucket[self.Id] = item
			self.id = self.Id + 1 

	def remove_item(self,Id):
		if Id in self.bucket:
			del self.bucket[Id]

class User(object):
	##create new user
	def __init__(self, name="", password=""):
		self.name = name
		self.password = password
	
	def return_name(self):
		return self.name

new_user = User()

@app.route('/')
def index():
	""" return the home page"""
	return render_template("index.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	"""return the signup page """
	form = RegisterForm()
	if form.validate_on_submit():
		new_user.name = form.username.data
		new_user.password = form.password.data
		return redirect(url_for('login'))
	return render_template("signup.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	"""return the login page"""	
	form = LoginForm()
	print(new_user.name, new_user.password)
	if form.validate_on_submit():
		if new_user.name == form.username.data:
			if new_user.password == form.password.data:
				return redirect(url_for('view'))
		else:
			return "<h1>Invalid username and password</h1>"
	return render_template("login.html", form=form)

@app.route('/view', methods=['GET', 'POST'])
def view():
	"""return the view page"""	
	if request.method == 'POST':
		requestDict = request.form.to_dict()
		print(requestDict)
		if requestDict['method'] == 'add':
			##get name of bucketlist from input
			new_bucket = Bucketlist(requestDict['data'])
			new_bucket.return_name()
			return jsonify(new_bucket.bucket)

		elif requestDict['method'] == 'create':
			#get the text from client and add it to bucket list
			
			text = ""
			for key in requestDict:
				text = key
			new_bucket.add_item(text)
			return jsonify(new_bucket.bucket)
		
		elif requestDict['method'] == 'delete':
			##id is gotten from the data sent from the client 
			new_bucket.remove_item(Id)

		elif requestDict['method']== 'read':
			#return the bucket
			return jsonify(new_bucket.bucket)
		
	else:
		return render_template('view.html')

if __name__ == "__main__":
	app.run(debug=True)