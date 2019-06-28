from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_user_signup_form():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def user_signup_complete():
    
    #Getting Form Info
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    switch = True

    username_error = ""
    password_error = "" 
    verify_error = ""
    email_error = ""

    def required(name):
        if name == "" :
            error = "This is a required field, please fill it out!"
        else:
            error = ""
        return error

    def lenth(name):
        if len(name) < 3 or len(name) > 21 :
            error = "You must have at least 3 characters but no more than 20"
        else:
            error = ""
        return error

    def space(name):
        if " " in name :
            error = "This feild can not contain spaces!"
        else:
            error = ""
        return error

    def atine(name):
        if name.count("@") < 1:
            error = "You need an @ at sign in your e-mail!"
        else:
            error = ""
        return error

    def ats(name):
        if name.count("@") > 1:
            error = "You can only have one @ at sign in your e-mail!"
        else:
            error = ""
        return error

    def dot(name):
        if name.count(".") < 1:
            error = "You need a . dot in your e-mail!"
        else:
            error = ""
        return error

    def dots(name):
        if name.count(".") > 1:
            error = "You can only have one . dot in your e-mail!"
        else:
            error = ""
        return error

    #UserName
    if username_error == "" :
        username_error = required(username)
    if username_error == "" :
        username_error = lenth(username)
    if username_error == "" :
        username_error = space(username)
    if username_error != "" :
        switch = False

    #Password
    if password_error == "" :
        password_error = required(password)
        verify_error = required(password)
    if password_error == "" :
        password_error = lenth(password)
        verify_error = lenth(password)
    if password_error == "" :
        password_error = space(password)
        verify_error = space(password)
    if password != verify :
        password_error = "Password and Verifacation do not match!"
        verify_error = "Password and Verifacation do not match!"
    if password_error != "" :
        switch = False

    #Email
    if email != "" :
        if email_error == "":
            email_error = atine(email)
        if email_error == "":
            email_error = ats(email)
        if email_error == "":
            email_error = dot(email)
        if email_error == "":
            email_error = dots(email)
        if email_error == "":
            email_error = lenth(email)
        if email_error == "":
            email_error = space(email)
        if email_error != "":
            switch = False

    if switch == True:
        username = username
        return redirect('/welcome?username={}'.format(username))

    else:
        return render_template('form.html', username_error=username_error, username=username, password_error=password_error, password=password, verify_error=verify_error, verify=verify, email_error=email_error, email=email)

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()