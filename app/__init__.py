#where we will initialize our application
from flask import Flask

# Initializing application
app = Flask(__name__)

from app import views