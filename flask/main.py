from flask import Flask, make_response, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    if user_ip != None:
        return
    return render_template('hello.html', user_ip=user_ip)