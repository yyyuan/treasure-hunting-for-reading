# models.py

from app import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    points_redeemed = db.Column(db.Integer)
    current_points = db.Column(db.Integer)
    teacher = db.Column(db.String)
    volunteer = db.Column(db.String)
