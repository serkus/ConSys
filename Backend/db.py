#-*- coding: UTF-8 -*-
#!/usr/bin/env python3

#from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class Tasks(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer(), primary_key=True)
    contID = db.Column(db.Integer(), primary_key=True)
    weg = db.Column(db.Float, privary_key=False)
    wrapperClass = db.Column(db.String(255), nullable=False)
    LevelName = db.Column(db.Text(), nullable=False)
    inOn = db.Column(db.DateTime(), default=datetime.utcnow)
    outOn = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    #def __repr__(self):
	#	return "<{}:{}>".format(self.id,  self.comnt.ID[:10])


	
class User(db.Model):
	__tablename__ = 'user'
	username = db.Column(db.Srting(255),  nullable=False)
	password = db.Column(db.Srting(255),  nullable=False)