import re
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
# Store Schema name in Variable
SCHEMA = "solo_project"
# Email/Password authentication
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
INVALID_PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
# Initialize Flask application
app = Flask(__name__)
# Initalize password security
bcrypt = Bcrypt(app)
# Required
app.secret_key = "$$$hoiimtemmie0$$$$"

# Applicaiton Routes. Default is GET

# Inital/Default Route


@app.route('/')
# renders login page, refered to as 'index'
def index():
    return render_template('index.html')

# Validate and Create new user from Form Data


@app.route('/users/create', methods=['POST'])
def users_new():
    valid = True  # assumes input is valid

    # validations

    if len(request.form['name']) < 2:
        flash("User name must be at least 2 characters")
        valid = False

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid")
        valid = False

    if len(request.form['pw']) < 8:
        flash("Password must be at least 8 characters")
        valid = False

    if INVALID_PASSWORD_REGEX.match(request.form['pw']):
        flash("Password must have at least one uppercase character and at least one number")
        valid = False

    if request.form['pw'] != request.form['confirm_pw']:
        flash("Passwords must match")
        valid = False

    # query db for duplicate email
    db = connectToMySQL(SCHEMA)
    validate_email_query = 'SELECT id FROM users WHERE email=%(email)s;'
    form_data = {
        'email': request.form['email']
    }
    existing_users = db.query_db(validate_email_query, form_data)

    if existing_users:
        flash("Email already in use")
        valid = False

    if not valid:
        # redirect to the form page, don't create user
        return redirect('/')

    # hash user's password
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])

    # create a user and log them in
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO users (name, email, password) VALUES (%(name)s, %(mail)s, %(pw)s);"
    data = {
        'name': request.form['name'],
        'mail': request.form['email'],
        'pw': pw_hash
    }
    user_id = db.query_db(query, data)

    # add user_id to session
    session['user_id'] = user_id
    print("*"*50)
    print(f"User id: {session['user_id']} added to session!")
    print("Redirecting to /gigs . . .")
    return redirect('/gigs')

# Validate user login by comparing formdata to userdata in database


@app.route("/login", methods=["POST"])
def login_user():
    is_valid = True  # Assumes input is Truthy

    # Compares POST data to Form Validation (input length, passowrd/email format regex {line 7,8})
    if len(request.form['email']) < 1:
        is_valid = False
        flash("Please enter your email")
    if len(request.form['password']) < 1:
        is_valid = False
        flash("Please enter your password")

    # If falsey, redirect to index, flash errors {line 96, line 99} render
    if not is_valid:
        return redirect("/")
    # If truthy, connect to database, compare formdata vs userdata in db.
    else:
        # variable representing call to db
        mysql = connectToMySQL(SCHEMA)
        # variable storing a dictonary with single key-value pair, assigning email to the email section of our form data
        data = {
            'email': request.form['email']
        }
        # String representing our SQL query asking to retrieve all of the users whose email matches the data variable
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        # Because user emails must be unique, our query will return an array with a single user object, assigned to the user variable
        user = mysql.query_db(query, data)
        # Validates password data from database (which is stored in the user variable)
        if user:
            # stores hashed pw from db
            # Remember, our obejct is stored in an Array!
            hashed_password = user[0]['password']

            # checks if hashed password stored in user variable matches the hashed formdata password
            if bcrypt.check_password_hash(hashed_password, request.form['password']):
                # If truthy, store user_id in session, print message to console, and redirect to /gigs route
                session['user_id'] = user[0]['id']
                user_id = session['user_id']
                print("*"*50)
                print(
                    f'Login successful! User {user_id} added to session. Redirecting . . .')
                return redirect("/gigs")
            # if pw invalid, redirect to index, render flash messages
            else:
                flash("Password is invalid")
                return redirect("/")
        # If email invalid, redirect to index, render flash messages
        else:
            flash("Please use a valid email address")
            return redirect("/")

# Logout, clears session, returns to index.


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Home page after user login/register


@app.route("/gigs")
# Checks if user is logged in by checking if id has been stored in session, an artifact of our validation function {line 128}
def allGigs():
    if 'user_id' not in session:
        print("*"*50)
        print("Id not in session, access denied!")
        flash("Please Login/Register")
        return redirect('/')
    # If user in session, query our db for gigs
    else:
        # variable storing call to db
        mysql = connectToMySQL('solo_project')
        # variable storring array of all gigs, retrieved from db using querey requesting all gigs and ordering them oldest to newest
        gigs = mysql.query_db('SELECT * FROM gigs ORDER BY date ASC')
        # call to db
        mysql = connectToMySQL(('solo_project'))
        # variable storing logged in user retrieved from query requesting all users whose id matches the id stored in session
        user = mysql.query_db(
            'SELECT * FROM users WHERE id = {}'.format(session['user_id']))
        # returns html page with template variables
        print("*"*50)
        print("Rendering viewAll.html. . .")
        return render_template('viewAll.html', gigs=gigs, user=user[0])

# Route to RSVP to gig
@app.route("/gigs/<id>/rsvp")
def rsvp(id):
    # call to db
    mysql = connectToMySQL(SCHEMA)
    # variable with dictionary representing userid and gigid
    data = {
        'user_id': session['user_id'],
        'gigs_id': id
    }
    # variable storing query inserting user_id and gig_ id into the rsvp table
    query = "INSERT INTO rsvp (users_id, gigs_id) VALUES (%(user_id)s, %(gigs_id)s)"
    mysql.query_db(query, data)
    return redirect(f"/gigs/{id}")

# Un-RSVP to gig
@app.route("/gigs/<id>/un_rsvp")
def un_rsvp(id):
    mysql = connectToMySQL(SCHEMA)
    query = "DELETE FROM rsvp WHERE users_id = %(user_id)s AND gigs_id = %(gig_id)s"
    data = {
        'user_id': session['user_id'],
        'gig_id': id
    }
    mysql.query_db(query, data)
    return redirect(f"/users/{session['user_id']}")

# Route to render user profile page
@app.route("/users/<id>")
def userGigs(id):
    if 'user_id' not in session:
        flash("Please Login/Register")
        return redirect('/')
    else:
        mysql = connectToMySQL(SCHEMA)
        user = mysql.query_db(
            'SELECT * FROM users WHERE id = {}'.format(session['user_id']))
        mysql = connectToMySQL(SCHEMA)
        gigs = mysql.query_db(
            'SELECT * FROM rsvp JOIN gigs ON rsvp.gigs_id = gigs.id WHERE users_id = {} ORDER BY gigs.date ASC'.format(id))
        print(gigs)
        return render_template('userEvents.html', user=user[0], gigs=gigs)

# Render gig profile page
@app.route("/gigs/<id>")
def viewOne(id):
    if 'user_id' not in session:
        flash("Please Login/Register")
        return redirect('/')
    else:
        # Get the gig
        mysql = connectToMySQL(SCHEMA)
        gig = mysql.query_db('SELECT * FROM gigs WHERE id = {}'.format(id))
        print(gig[0]['creator_id'])
        mysql = connectToMySQL(SCHEMA)
        user = mysql.query_db(
            'SELECT * FROM users WHERE id = {}'.format(session['user_id']))
        print(user[0]['name'])
        mysql = connectToMySQL(SCHEMA)
        attendees = mysql.query_db(
            'SELECT users.name from rsvp JOIN users ON rsvp.users_id = users.id WHERE gigs_id = {}'.format(id))
        # connnect to db and store creator object in variable
        mysql = connectToMySQL(SCHEMA)
        creator = mysql.query_db('SELECT * FROM users WHERE id = {}'.format(gig[0]['creator_id']))
        print(creator[0]['name']);
        return render_template('viewOne.html', gig=gig[0], user=user[0], creator = creator[0], attendees=attendees)

# Render new gig form 
@app.route("/gigs/new")
def newGig():
    if 'user_id' not in session:
        flash("Please Login/Register")
        return redirect('/')
    else:
        mysql = connectToMySQL('solo_project')
        user = mysql.query_db(
            'SELECT * FROM users WHERE id = {}'.format(session['user_id']))
        return render_template('addNew.html', user=user[0])

# Validate form data and create new gig in db
@app.route("/gigs/create", methods=['POST'])
def createGig():
    valid = True

    if len(request.form['name']) < 2:
        flash("Gig name must be at least 2 characters")
        valid = False

    if len(request.form['location']) < 2:
        flash("Gig location must be at least 2 characters")
        valid = False

    if len(request.form['date']) < 2:
        flash("A date is required")
        valid = False

    if not valid:
        return redirect("/gigs/new")

    mysql = connectToMySQL(SCHEMA)
    query = 'INSERT INTO gigs (name, location, date, description, creator_id) VALUES (%(name)s, %(location)s, %(date)s, %(description)s, %(id)s)'
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "date": request.form['date'],
        "description": request.form['description'],
        "id": session['user_id']
    }
    gig = mysql.query_db(query, data)
    return redirect("/gigs")

# Delete gig
@app.route("/gigs/<id>/delete")
def deleteGig(id):
    mysql = connectToMySQL(SCHEMA)
    gig = mysql.query_db('DELETE FROM gigs WHERE id = {} '.format(id))
    return redirect('/gigs')

# Render edit page
@app.route("/gigs/<id>/edit")
def editGig(id):
    if 'user_id' not in session:
        flash("Please Login/Register")
        return redirect('/')
    else:
        mysql = connectToMySQL(SCHEMA)
        gig = mysql.query_db('SELECT * FROM gigs WHERE id = {}'.format(id))
        mysql = connectToMySQL(SCHEMA)
        user = mysql.query_db(
            'SELECT * FROM users WHERE id = {}'.format(session['user_id']))
        return render_template("edit.html", gig=gig[0], user=user[0])

# Validate form data and query db 
@app.route("/gigs/<id>/update", methods=['POST'])
def update(id):
    valid = True

    if len(request.form['name']) < 2:
        flash("Gig name must be at least 2 characters")
        valid = False

    if len(request.form['location']) < 2:
        flash("Gig location must be at least 2 characters")
        valid = False

    if len(request.form['date']) < 2:
        flash("A date is required")
        valid = False

    if not valid:
        return redirect("/gigs/<id>/edit")

    mysql = connectToMySQL(SCHEMA)
    query = 'UPDATE gigs SET name = %(name)s, location = %(location)s , date = %(date)s, description = %(description)s WHERE id = {}'.format(
        id)
    data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "date": request.form['date'],
        "description": request.form['description'],
    }
    gig = mysql.query_db(query, data)
    return redirect("/gigs")

# required initalizes Flask App 
if __name__ == "__main__":
    app.run(debug=True)
