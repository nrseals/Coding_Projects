# Imports
import re
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
from datetime import datetime

# SCHEMA NAME, Regex for email/pw validation
SCHEMA = "eCommerce"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
INVALID_PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')

# initalize app, bcrypt, secret key
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfqwerzxcv"


# Begin Routes

# Index Route, Login Page
@app.route("/")
def index():
    return render_template("index.html")

# Registration Page
@app.route("/users/register")
def register():
    return render_template("register.html")

# Validate Form info, Add User to db, redirect to index
@app.route("/users/new", methods = ['POST'])
def createUser():
    # Names
    valid = True
    if len(request.form['fname'])< 2 or len(request.form['lname']) < 2 or len(request.form['username']) < 2:
        flash("Names must be at least 2 characters")
        valid = False
    #Unique username
    db = connectToMySQL(SCHEMA)
    data = {
        "provided_username": request.form['username']
    }
    query = "SELECT id FROM users WHERE username=%(provided_username)s"
    existing_usernames = db.query_db(query, data)
    if existing_usernames:
        flash("Username already exists")
        valid = False
    # Email
    # Format
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email")
        valid = False
    # Unique 
    db = connectToMySQL(SCHEMA)
    data = {
        'email': request.form['email']
    }
    query = "SELECT id FROM users WHERE email=%(email)s;"
    existing_users = db.query_db(query, data)
    if existing_users:
        flash("Email already in use")
        valid = False
    # Password
    if len(request.form['pw']) < 8:
        flash("Password must be at least 8 characters")
        valid = False
    if request.form['pw'] != request.form['confirm_pw']:
        flash("Passwords must match")
        valid = False
    if INVALID_PASSWORD_REGEX.match(request.form['pw']):
        flash("Password must have at least one uppercase character and at least one number")
        valid = False
    # If not valid, redirect to index w/messages
    if not valid:
        return redirect('/users/register')

    # Code beyond this point will execute only if user input is valid

    # hash users pw
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    # create user in db
    db = connectToMySQL(SCHEMA)
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'un': request.form['username'],
        'em': request.form['email'],
        'pw_hash': pw_hash
    }
    query = "INSERT INTO users (f_name, l_name, username, email, pw_hash) VALUES (%(fn)s, %(ln)s, %(un)s, %(em)s, %(pw_hash)s);"
    user = db.query_db(query, data)
    print("*"*50)
    print(f"Success! User added to db! ")
    flash("Registration Successful! Please Log in!")
    return redirect("/")

# Login - validate user info, add id to session, redirect to success page
@app.route("/users/login", methods = ['POST'])
def login():
    valid = True
    if len(request.form['username']) < 1:
        flash("Please enter your Username")
        valid = False
    if len(request.form['pw']) < 1:
        flash("Please enter your password")
        valid = False
    if not valid:
        return redirect("/")
    else:
        db = connectToMySQL(SCHEMA)
        data = {
            'un': request.form['username']
        }
        query = "SELECT * FROM users WHERE username=%(un)s;"
        user = db.query_db(query, data)
        if user:
            hashed_pw = user[0]['pw_hash']
            if bcrypt.check_password_hash(hashed_pw, request.form['pw']):
                session['logged_user_id'] = user[0]['id']
                print("*"*50)
                print(f"User {session['logged_user_id']} logged in!")
                return redirect("/products")
            else:
                flash("Password is invalid")
                return redirect("/")
        else:
            flash("Please use a valid username")
            return redirect("/")

# Logout Route
@app.route("/users/logout")
def logout():
    print("*"*50)
    print(f"User {session['logged_user_id']} logged out!")
    session.clear
    return redirect("/")

# Main page
@app.route("/products")
def products():
    if 'logged_user_id' not in session:
        flash("Please Log in")
        return redirect("/")
    db = connectToMySQL(SCHEMA)
    data = {
        's': session['logged_user_id']
    }
    query = "SELECT * FROM users WHERE id = %(s)s"
    user = db.query_db(query, data)

    return render_template("success.html", user = user[0])


# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)