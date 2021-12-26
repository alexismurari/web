from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opensource')
def open():
    return render_template('open.html')

@app.route('/projects')
def project():
    return render_template('projects.html')

@app.route('/opensource')
def contact():
    return render_template('contact.html')