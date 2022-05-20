from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    '''Home do serviço'''
    return render_template('index.html')


@app.route('/anderson')
def anderson():
    '''Backend anderson'''
    return render_template('anderson.html')
