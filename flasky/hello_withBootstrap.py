from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

# @app.route('/')
# def index():
#    return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#    return '<h1>Hello %s!</h1>' % name

@app.route('/')
def index():
   return render_template('index.html',
                           current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
   return render_template('user_withBootstrap.html', name=name)

# @app.route('/<name>')
# def userpage(name):
#    return '<h1>Hello %s. Here is your page</h1' % name

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html', e=e), 404

@app.errorhandler(500)
def internal_server_error(e):
   return render_template('500.html'), 500

if __name__ == '__main__':
##   app.run(debug=True)
   manager.run()
   
