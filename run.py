import os
from os import environ
import sys
sys.path.append(os.getcwd())
from app import app

app.run(debug=False,host='0.0.0.0',port=environ.get("PORT", 5000))