# export FLASK_APP=project.py
# export FLASK_DEBUG=1
# flask run
"""
Name: Brian Palomar
Teammates: Nick Mederos, Vicente Valencia & team number 7327 
CST205-01_SP22: Multimedia Design & Progmng
"""
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Home Page
@app.route('/')
def home():
  return render_template('index.html')


# Get im id after page2/
# Page 2
@app.route('/image1')
def page2func(image_id):
  return render_template('page2.html')

# Page 3
@app.route('/image2')
def page3func(image_id):
  return render_template('page3.html')

# Page 4
@app.route('/image3')
def page4func(image_id):
  return render_template('page4.html')
