"""
Storing the information on database models
"""
from . import db
from sqlalchemy.sql import func


class Purchase(db.Model):
    """
    Records for the purchase
    """
    __tablename__ = 'purchases'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=func.now())
    farmer_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    cost_per_kg = db.Column(db.Float, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
