from flask import Flask, render_template
app = Flask(__name__)

def bold_text(func):
    def wrap():
        return '<b>{}</b>'.format(func())
    return wrap

@app.route('/foo/<name>')
def foo(name):
	return render_template("index.html", to=name)

@app.route('/log')
def index():
    return 'Hello world'

@app.route('/whereami')
def whereami():
    return 'Ghana'

@app.route('/greetings')
@bold_text
def hello_world():
    return '<p>Hello World</p>'

@app.route('/bold')
def hello_worldbold():
    return '<b>Hello World</b>'

@app.route('/info/<name>/<age>')
def your_info(name,age):
    return '<p>Your name is {} and your age is {} years</p>'.format(name, age)


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
    
