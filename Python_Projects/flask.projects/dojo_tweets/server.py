import re
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

SCHEMA = "dojo_tweets"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
INVALID_PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfqwerzxcv"

# Routes

# Index route, login
@app.route("/")
def index():
    return render_template("index.html")

# Registration form
@app.route("/register")
def register():
    return render_template("register.html")

# Validate new user and add to db
@app.route("/users/new", methods=['POST'])
def createUser():
    valid = True
    # First Name - length
    if len(request.form['fname']) < 2:
        flash("Name must be at least 2 characters")
        valid = False
    # Last Name - length
    if len(request.form['lname']) < 2:
        flash("Names must be at least 2 characters")
        valid = False
    # Email - length, format, unique
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be vaild")
        valid = False
    #Query db for duplicate email
    db = connectToMySQL(SCHEMA)
    data = {
        'email': request.form['email']
    }
    query = "SELECT id FROM users WHERE email=%(email)s;"
    existing_users = db.query_db(query, data)
    #Validate unique email
    if existing_users:
        flash("Email already in use")
        valid = False
    #Pw - length, matches confirm pw
    if len(request.form['pw']) < 8:
        flash("Password must be at least 8 characters")
        valid = False
    if INVALID_PASSWORD_REGEX.match(request.form['pw']):
        flash("Password must have at least one uppercase character and at least one number")
        valid = False
    if request.form['pw'] != request.form['confirm_pw']:
        flash("Passwords must match")
        valid = False

    #If not valid, redirect, display flash errors, don't add data to db
    if not valid:
        return redirect('/')
    
    #hash user's Pw
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])

    #create user in db, redirect to login
    db = connectToMySQL(SCHEMA)
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['email'],
        'hashed_pw': pw_hash
    }
    query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(fn)s,%(ln)s,%(em)s,%(hashed_pw)s);"
    user = db.query_db(query, data)
    flash("Registration successful! Please Log in!")
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
