#TODO: Delete this file. It has been replaced with app.py

from theapp import models as app
from flask import render_template
from flask_bootstrap import Bootstrap

@app.route('/')
def index():
    return render_template('index.html')

