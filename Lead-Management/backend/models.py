from app import db

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='New')
    date_added = db.Column(db.DateTime, default=db.func.now())
    last_updated = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
