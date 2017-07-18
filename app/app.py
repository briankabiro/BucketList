from flask import Flask,render_template,request
app = Flask(__name__,static_url_path='/static',static_folder="../static",template_folder='../templates')

class Bucketlist():
	def __init__(self,name,id=0,bucket={}):
		self.name = name
		self.id = id
		self.bucket = bucket 
	def print_name(self):
		return self.name
	def __del__(self):
		return True
	def add_item(self,item):
		if self.id not in self.bucket:
			self.bucket[self.id] = item
			self.id = self.id + 1 
	def remove_item(self,index):
		if index in self.bucket:
			del self.bucket[index]


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/signup')
def signup():
	return render_template("signup.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/view')
def view():
	return render_template('view.html')

@app.route('/validate', methods = ['POST'])
def validate():
	if request.method == 'POST':
		data = request.form
		print(data)
		return render_template("view.html")

if __name__ == "__main__":
	app.run()