from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Nathan'}
    posts = [
        {
            'author': {'username': 'Nathan'},
            'body': 'This is a test post'
        },
        {
            'author': {'username': 'John'},
            'body': 'This is another test post'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
