from flask import Flask, session, render_template, redirect, request
from json import JSONEncoder, JSONDecoder, JSONDecodeError
app = Flask(__name__)
app.template_folder = 'websiteGGG'

@app.route('/')
def homepage():
    return render_template('HomePage.html')

@app.route('/image/<path>')
def imagepath(path):
    print(path)
    # Open the file in read mode
    file = open('websiteGGG/'+path, "r")
    # Read the entire content of the file
    content = file.read()
    # Print the content
    # Close the file
    file.close()
    return file

if __name__ == '__main__':
    app.run(debug=True)