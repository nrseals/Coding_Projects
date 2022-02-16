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

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)