from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)

# @app.route('/')
# def index():
#    return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#    return '<h1>Hello %s!</h1>' % name

@app.route('/index')
def index():
   return render_template('index.html',
                           current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
   return render_template('user.html', name=name)

@app.route('/<name>')
def userpage(name):
   return '<h1>Hello %s. Here is your page</h1' % name

if __name__ == '__main__':
##   app.run(debug=True)
   manager.run()
   
