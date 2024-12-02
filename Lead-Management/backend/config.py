import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'  # Local SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable unnecessary features of SQLAlchemy

    # Email configuration
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Load from environment variable for security
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Load from environment variable for security
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')  # Default sender for emails

    # Secret key for session management and CSRF protection
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')  # Change to a strong secret key
