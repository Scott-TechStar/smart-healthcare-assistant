from src.app import db
from datetime import datetime

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    fever = db.Column(db.Boolean, nullable=True)
    cough = db.Column(db.Boolean, nullable=True)
    headache = db.Column(db.Boolean, nullable=True)
    chest_pain = db.Column(db.Boolean, nullable=True)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prediction = db.Column(db.String(100), nullable=False)
    prediction_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    user = db.relationship('UserProfile', back_populates='predictions')

UserProfile.predictions = db.relationship('Prediction', back_populates='user')
