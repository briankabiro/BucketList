import os
import sys
sys.path.append(os.getcwd())
from app import app
app.run(debug=True)