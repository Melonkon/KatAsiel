from core import db
from datetime import datetime

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    daily_food = db.Column(db.Float, nullable=False)

    def __init__(self, name, color, breed, daily_food):
        self.name = name
        self.color = color
        self.breed = breed
        self.daily_food = daily_food

class FeedingHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, db.ForeignKey('cat.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    food_consumed = db.Column(db.Float, nullable=False)

    cat = db.relationship('Cat', backref=db.backref('feeding_history', lazy=True))

    def __init__(self, cat_id, food_consumed, date=None):
        self.cat_id = cat_id
        self.food_consumed = food_consumed
        if date:
            self.date = date
