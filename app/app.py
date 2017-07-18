from flask import Flask,render_template
app = Flask(__name__,static_url_path='/static',static_folder="static")

class Bucketlist():
	def __init__(self,name,index=0,bucket={}):
		self.name = name
		self.index = index
		self.bucket = bucket 
	def print_name(self):
		return self.name
	def __del__(self):
		return True
	def add_item(self,item):
		if self.index not in self.bucket:
			self.bucket[self.index] = item
			self.index = self.index + 1 
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
	
if __name__ == "__main__":
	app.run()