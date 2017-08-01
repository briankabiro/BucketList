from flask import Flask
app = Flask(
    __name__,
    static_url_path='/static',
    static_folder="../static",
    template_folder='../templates')

app.config['SECRET_KEY'] = "secret_key"

from app import views
