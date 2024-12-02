from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_cors import CORS

# Initialize app and extensions
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Change to your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Change to your email password
mail = Mail(app)
CORS(app)

# Initialize the database
db = SQLAlchemy(app)

# Models and routes import
from models import Lead
from routes import *

if __name__ == "__main__":
    db.create_all()  # Create database tables
    app.run(debug=True)
