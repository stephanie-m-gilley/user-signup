from flask import Flask, request, redirect, render_template
import os
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error = ''
    verify_error = ''
    email_error = ''

    if len(username) > 20:
        user_error = "Username out of range"
        username = ''
    if len(username) < 3 and len(username) >= 1:
        user_error = "You need more characters"
        username = ''
    if len(username) is 0:
        user_error = "Can not be left blank"
        username = ''
    for char in username:
        if char.isspace():
            username = "Can not contain spaces"
            username = ''
    if not user_error:
        username = username        

    
    if len(password) > 20:
        pass_error = "Username out of range"
        password = ''
    if len(password) < 3 and len(password) >= 1:
        pass_error = "You need more characters"
        password = ''
    if len(password) is 0:
        pass_error = "Can not be left blank"
        password = ''
    for char in password:
        if char.isspace():
            pass_error = "Can not contain spaces"
            password = ''


    if password != verify:
        verify_error = "Passwords do not match or not valid"
        verify = ''

    for char in email:
        if email.count("@") > 1 or email.count(".") > 1:
            email_error = "Not a valid email"
            email = ''
    if len(email) < 3:
        email_error = "Email not in range"
        email = email
    if len(email) > 20:
        email_error = "Email out of range"
        email = email 
    for char in email:
        if char.isspace():
            email_error = "Can not contain spaces"
            email = email

    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('/home.html', username=username) 

    return render_template('index.html', username=username, user_error=user_error,
    password=password, pass_error=pass_error, verify_error=verify_error, verify=verify,
    email=email, email_error=email_error)


@app.route("/home", methods=['POST'])
def welcome():
    return render_template('home.html')


app.run()