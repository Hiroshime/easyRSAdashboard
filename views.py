from flask import render_template, request, redirect, session, flash, url_for
from dashboard import app , db
from models import *


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lista')
def index():
    return render_template('index.html')
