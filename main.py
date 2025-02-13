from flask import Flask, session, render_template, redirect, request, send_from_directory
from json import JSONEncoder, JSONDecoder, JSONDecodeError
app = Flask(__name__)
app.template_folder = 'websiteGGG'

@app.route('/')
def homepage():
    return render_template('HomePage.html')

@app.route('/files/<path>')
def downloadfile(path):
    print(path)
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)