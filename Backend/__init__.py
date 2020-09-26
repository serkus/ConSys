#-*- coding: utf-8 -*-
#!/usr/bin/env python3

from flask import Flask
#from forms import ContactForm
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = "./db"
#manager = Manager(app)
#db = SQLAlchemy(app)

from Backend import routes
