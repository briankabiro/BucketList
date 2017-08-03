import os
import sys
sys.path.append(os.getcwd())
from app import app

app.run(host='0.0.0.0',port=environ.get("PORT", 5000))