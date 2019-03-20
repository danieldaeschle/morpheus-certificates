from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(50), nullable=False)
    issue_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.String(80), nullable=False)
    token = db.Column(db.String(100), nullable=False, unique=True)
    link = db.Column(db.String(200), nullable=True)
    approved_by = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
