from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the app and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Make sure to use your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # You need a secret key for sessions

# Initialize the database
db = SQLAlchemy(app)
