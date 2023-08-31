from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_database = [{
    "username" : 'listo@gmail.com',
    "password" : 'what123'
}]



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')
    password = request.form.get('password')
    for users in users_database:
        if users['username'] == "listo@gmail.com" and users['password'] == "what123":
            return "login successful"
        else:
            return "login failed"
    



if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
