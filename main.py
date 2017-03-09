from flask import Flask
from flask import redirect
app = Flask(__name__)

#Basic route
@app.route('/')

#default method to show
def index():
	return '<h1>Hello World!</h1>'

#http://localhost:5000/yourname
# @app.route('/<name>')
# def user(name):
# 	return '<h1>Hello, %s!</h1>' % name

#http://localhost:5000/yourname
@app.route('/user/<name>')
def user(name):
	return redirect('http://www.google.com')




if __name__ == '__main__':
	app.run(debug=True)