from app import db
from datetime import datetime

class ModelData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False, default="salary")
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    type = db.Column(db.String(20), nullable=False)
    
    def __str__(self):
        return self.id