# export FLASK_APP=project.py
# export FLASK_DEBUG=1
# flask run
"""
Name: Brian Palomar
Teammates: Nick Mederos, Vicente Valencia & team number 7327 
CST205-01_SP22: Multimedia Design & Progmng
"""
# image_info.py route is static/images/hw3_images/image_info
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from image_info import image_info
import random

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Makes sure things are working
# print(image_info[0]['title'])

# Randomizer 
random.shuffle(image_info)

# Grabs first 3 images after randomized
im1 = image_info[0]['title']
im1_id = image_info[0]['id']
im1_user = image_info[0]['flickr_user']

im2 = image_info[1]['title']
im2_id = image_info[1]['id']
im2_user = image_info[1]['flickr_user']

im3 = image_info[2]['title']
im3_id = image_info[2]['id']
im3_user = image_info[2]['flickr_user']

# Makes sure randomizer works
# print(image_info)
# print(im2)
# print(im3)

# Home Page
@app.route('/')
def home():
  return render_template('index.html', im1=im1, im1_id=im1_id,
   im2=im2, im2_id=im2_id, im3=im3, im3_id=im3_id)


# Get im id after page2/
# Page 2
@app.route('/image1/<image_id>')
def page2func(image_id):
  return render_template('page2.html', im1=im1, im1_id=im1_id, im1_user=im1_user)

# Page 3
@app.route('/image2/<image_id>')
def page3func(image_id):
  return render_template('page3.html', im2=im2, im2_id= im2_id, im2_user=im2_user)

# Page 4
@app.route('/image3/<image_id>')
def page4func(image_id):
  return render_template('page4.html', im3=im3, im3_id=im3_id, im3_user=im3_user)
