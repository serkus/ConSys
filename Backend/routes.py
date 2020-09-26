#-*- coding: UTF-8 -*-
#!/usr/bin/env python3

from Backend import app
from flask import render_template
#from flask_sqlalchemy import SQLAlchemy
from Backend.db import Tasks
import os, json
 
@app.route('/')
@app.route('/index')
def index():
	#user = {'username': "user"/, 'paswd'":1234567"}
	return render_template('index')

# проверить пустой ли контейнер
app.route('/tasks')
def EmtryCont():
	tasks = Tasks.get()
	return tasks

@app.route("auth")
def Auth():
	return render_template('auth.html')

@app.route('/get_info_Containter')
def getInfoConteiner():
	pass
