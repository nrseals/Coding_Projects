import re
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
from datetime import datetime

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
    # Query db for duplicate email
    db = connectToMySQL(SCHEMA)
    data = {
        'email': request.form['email']
    }
    query = "SELECT id FROM users WHERE email=%(email)s;"
    existing_users = db.query_db(query, data)
    # Validate unique email
    if existing_users:
        flash("Email already in use")
        valid = False
    # Pw - length, matches confirm pw
    if len(request.form['pw']) < 8:
        flash("Password must be at least 8 characters")
        valid = False
    if INVALID_PASSWORD_REGEX.match(request.form['pw']):
        flash("Password must have at least one uppercase character and at least one number")
        valid = False
    if request.form['pw'] != request.form['confirm_pw']:
        flash("Passwords must match")
        valid = False

    # If not valid, redirect, display flash errors, don't add data to db
    if not valid:
        return redirect('/')

    # hash user's Pw
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])

    # create user in db, redirect to login
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

# Login - validate user input. if successfull, add info to session and redirect to homepage, if not, redirect to index with flash errors


@app.route("/users/login", methods=['POST'])
def login():
    # Validate user input
    valid = True
    # Validate input length
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please enter your email")
    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please enter your password")
    # If not valid, return to index
    if not valid:
        return redirect("/")
    # If length is valid, compare input to db and validate
    else:
        # query db to see if user email exists
        db = connectToMySQL(SCHEMA)
        data = {
            'em': request.form['email']
        }
        query = "SELECT * FROM users WHERE email = %(em)s;"
        # Result of Query is a List of dictonaries. Because email must be unique, there should only be one object that we store in the user variable
        user = db.query_db(query, data)
        # if user email exists and is unique then check pw
        if user:
            # Grab the stored hash from the db
            # User info stored in list of objects, hence we refer to it as user[0]
            hashed_pw = user[0]['password']
            # hash and compare the user input password to the stored hash
            if bcrypt.check_password_hash(hashed_pw, request.form['password']):
                # if valid, add info to session, print message to console, redirect
                session['user_id'] = user[0]['id']
                user_id = session['user_id']
                print("*"*50)
                print(
                    f'Login successful! User {user_id} added to session. Redirecting . . .')
                return redirect("/tweets")
            else:
                flash("Password is invalid")
                return redirect("/")
        # If email check fails
        else:
            flash("Please use a valid email address")
            return redirect("/")

# Logout - clears session


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Homepage


@app.route('/tweets')
def tweets():
    # If user is not logged in, redirect to index
    if 'user_id' not in session:
        flash("Please log in to view Tweets")
        return redirect("/")
    # connect to db, retrive user object from db using the session id

    db = connectToMySQL(SCHEMA)
    data = {
        's': session['user_id']
    }
    # even though this is only one object, it's given to us in a list from SQL. Must be accessed with syntax "user[0]"
    query = "SELECT * from users WHERE id = %(s)s"
    user = db.query_db(query, data)
    # connect to db retrieve tweets with their username from db
    db = connectToMySQL(SCHEMA)
    query = "SELECT tweets.users_id, tweets.id as tweet_id, users.first_name, users.last_name, tweets.body, tweets.created_at, COUNT(tweets_id) as times_liked FROM liked_tweets RIGHT JOIN tweets ON tweets.id = liked_tweets.tweets_id JOIN users ON tweets.users_id = users.id  GROUP BY tweets.id ORDER BY tweets.created_at DESC"
    tweets = db.query_db(query)

    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM liked_tweets WHERE users_id = %(user_id)s"
    data = {
        'user_id': session['user_id']
    }
    liked_tweets = [tweet['tweets_id'] for tweet in db.query_db(query, data)]
    for tweet in tweets:
        print(datetime.now())
        time_since_posted = datetime.now() - tweet['created_at']
        days = time_since_posted.days
        hours = time_since_posted.seconds//3600
        minutes = (time_since_posted.seconds//60) % 60
        if tweet['tweet_id'] in liked_tweets:
            tweet['already_liked'] = True
        else:
            tweet['already_liked'] = False

        tweet['time_since_posted'] = (days, hours, minutes)

    return render_template("tweets.html", user=user[0], tweets=tweets)

# Tweet Creation


@app.route("/tweets/create", methods=['POST'])
def saveTweet():
    if 'user_id' not in session:
        return redirect("/")
    # validate
    valid = True
    if len(request.form['body']) < 1:
        valid = False
        flash("Tweet cannot be blank")
    if len(request.form['body']) > 250:
        valid = False
        flash("Tweet cannot have more than 250 characters")
    # connect to db, insert query, redirect
    if valid:
        db = connectToMySQL(SCHEMA)
        data = {
            'id': session['user_id'],
            'b': request.form['body']
        }
        query = "INSERT INTO tweets (body, users_id) VALUES (%(b)s, %(id)s )"
        tweet = db.query_db(query, data)
        return redirect("/tweets")

# Add Like


@app.route("/tweets/<tweet_id>/add_like")
def addLike(tweet_id):
    # connect to db
    db = connectToMySQL(SCHEMA)
    data = {
        'user_id': session['user_id'],
        'tweet_id': tweet_id,
    }
    query = "INSERT INTO liked_tweets (users_id, tweets_id) VALUES (%(user_id)s, %(tweet_id)s)"
    like = db.query_db(query, data)
    return redirect("/tweets")

# App unlike


@app.route("/tweets/<tweet_id>/unlike")
def unlike_tweet(tweet_id):
    query = "DELETE FROM liked_tweets WHERE users_id = %(user_id)s AND tweets_id = %(tweet_id)s"
    data = {
        'user_id': session['user_id'],
        'tweet_id': tweet_id
    }
    mysql = connectToMySQL('dojo_tweets')
    mysql.query_db(query, data)
    return redirect("/tweets")

# Delete tweet


@app.route("/tweets/<tweet_id>/delete")
def delete_tweet(tweet_id):

    # if ON DELETE CASCADE is not set up for tweets DELETE likes first
    query = "DELETE FROM liked_tweets WHERE tweets_id = %(tweet_id)s"
    data = {
        'tweet_id': tweet_id
    }
    mysql = connectToMySQL('dojo_tweets')
    mysql.query_db(query, data)

    query = "DELETE FROM tweets WHERE id = %(tweet_id)s"
    mysql = connectToMySQL('dojo_tweets')
    mysql.query_db(query, data)
    return redirect("/tweets")

# Edit tweet


@app.route("/tweets/<tweet_id>/edit")
def editTweet(tweet_id):
    # protect route - user must be signed in
    if 'user_id' not in session:
        return redirect("/")
    # load user
    db = connectToMySQL(SCHEMA)
    data = {
        'user_id': session['user_id']
    }
    query = "SELECT * FROM users WHERE id = %(user_id)s;"
    user = db.query_db(query, data)

    # load tweet from db
    db = connectToMySQL(SCHEMA)
    data = {
        'tweet_id': tweet_id,
    }
    query = "SELECT * FROM tweets WHERE id = %(tweet_id)s"
    tweet = db.query_db(query, data)
    # return template
    return render_template("edit.html", tweet=tweet[0], user=user[0])

# Update tweet


@app.route("/tweets/<tweet_id>/update", methods=["POST"])
def updateTweet(tweet_id):
    # validate inputs
    valid = True
    if len(request.form['body']) < 1:
        valid = False
        flash("Tweet cannot be blank")
    if len(request.form['body']) > 250:
        valid = False
        flash("Tweet cannot have more than 250 characters")
    # update info in db
    if valid:
        db = connectToMySQL(SCHEMA)
        data = {
            'body': request.form['body'],
            'tweet_id': tweet_id,
        }
        query = "UPDATE tweets SET body = (%(body)s) WHERE id = %(tweet_id)s;"
        update = db.query_db(query, data)
        return redirect("/tweets")

# Users page


@app.route("/users")
def users():
    # protected route
    if 'user_id' not in session:
        return redirect("/")
    # query logged user
    db = connectToMySQL(SCHEMA)
    data = {
        'logged_id': session['user_id']
    }
    query = "SELECT * FROM users WHERE id = %(logged_id)s "
    logged_user = db.query_db(query, data)
    # query db for all users
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users"
    users = db.query_db(query)
    # render template
    return render_template("/users.html", users=users, logged_user=logged_user[0])


# End of routes, initalize Flask app
if __name__ == "__main__":
    app.run(debug=True)