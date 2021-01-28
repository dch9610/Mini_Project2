import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Turn(db.Model):
    __tablename__ = 'Turnover'
    id=db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.String(32))
    major  = db.Column(db.String(32))
    edu_lev  = db.Column(db.String(32))
    re_exp = db.Column(db.String(32))
    last = db.Column(db.Integer)
    comp_type = db.Column(db.String(32))
    comp_size = db.Column(db.String(32))
    exp = db.Column(db.Integer)
