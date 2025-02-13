from flask import Flask, session, render_template, redirect, request
from json import JSONEncoder, JSONDecoder, JSONDecodeError
app = Flask(__name__)
app.template_folder = 'websiteGGG'

@app.route('/')
def homepage():
    return render_template('homepage.html')
