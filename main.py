from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route("/submit")
def index():
    return render_template("form.html")

def empty_blank(a):
    if a:
        return True
    else:
        return False

def character_len(a):
    if len(a) > 2 and len(a) <21:
        return True
    else :
        return False

def email_format_21(a):
    if a.count("@") >=1:
        return True
    else:
        return False

def email_format_22(a):
    if a.count("@") <=1:
        return True
    else :
        return False

def email_format_dot(a):
        if a.count(".") >=1:
        return True
    else:
        return False

def email_format_dot2(a):
    if a.count(".") <=1:
        return True
    else :
        return False


@app.route("/submit", methods=['POST'])
def fill_in():

    username = request.form['username']
    password = request.form['password']
    verify = request.form["verify"]
    email = request.form["email"]

    username_blank = ""
    password_blank = ""
    verify_blank = ""
    email_blank = ""

    error_needed = "This Field Is Required"
    error_count = "There Must Be Between 3 and 20 Characters"
    error_spaces = "There Must Be No Spaces"
    error_password = "Please Re Enter Your Password"

    if not empty_blank(password):
        password_blank = error_needed
        password = ""
        verify = ""
    elif not character_len(password):
        password_blank = "Password" + error_count
        password = ""
        verify = ""
        verify_blank = error_password
    else:
        if " " in password :
            password_blank = "Password " + error_spaces
            password = ""
            verify = ""
            verify_blank = error_password

    if password_blank != verify_blank:
        verify_


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html" , username = "username")

app.run()