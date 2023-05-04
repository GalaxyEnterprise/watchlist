# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask,render_template
from flask_moment import Moment
from markupsafe import escape
from datetime import datetime
app = Flask(__name__)
name = 'Nebula'
movies=[
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)
@app.route('/<name>')
def hello(name):
    return f'User:{escape(name)}'
if __name__ == '__main__':
    app.run(host="localhost",debug=True,port=8080)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
