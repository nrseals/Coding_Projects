from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    print("*"*50);
    print("Success! Redirecting . . .")

    return redirect("/users")

@app.route("/users")
def allUsers():
    print("*"*50);
    print("Retriving all friends from db")

    mysql = connectToMySQL('users')
    users= mysql.query_db('SELECT * FROM friends')

    print("*"*50);
    print("Success! Rendering template")

    return render_template("allUsers.html", users = users)

@app.route("/users/new")
def render_form():
    print("*"*50);
    print("Rendering form")

    return render_template("userForm.html")

@app.route("/users/create", methods=["POST"])
def add_friend_to_db():
    print("*"*50);
    print("Adding new user to db")

    mysql = connectToMySQL("users") 
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(email)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "email": request.form["email"]
    } 
    user_id = mysql.query_db(query, data)

    print("*"*50);
    print("User successfully added new user to db! redirecting . . .")

    return redirect("/users/{}".format(user_id))

@app.route("/users/<user_id>")
def getAndDisplayOne(user_id):
    print("*"*50);
    print("Fetching one user from db")

    mysql = connectToMySQL("users")
    query = "SELECT * FROM friends WHERE idfriends = %(id)s"
    data = {
        "id" : user_id
    }
    user= mysql.query_db(query, data)

    print("*"*50);
    print(user)

    print("*"*50);
    print("Success! Rendering template")

    return render_template("oneUser.html", user = user[0] )

@app.route("/users/<user_id>/edit")
def render_update_form(user_id):
    print("*"*50);
    print("Fetching user for update from db")

    mysql = connectToMySQL("users")
    query = "SELECT * FROM friends WHERE idfriends = %(id)s"
    data = {
        "id" : user_id
    }
    user= mysql.query_db(query, data)

    print("*"*50);
    print(user);

    print("*"*50);
    print("Success! Rendering template");

    return render_template("editUser.html", user = user[0])

@app.route("/users/<user_id>/update", methods = ["POST"])
def update_user(user_id):
    print("*"*50);
    print("Updating user in db")

    mysql = connectToMySQL("users")
    query = "UPDATE friends SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, updated_at=NOW()"
    data = {
        "fn" : request.form['fname'],
        "ln" : request.form['lname'],
        "em" : request.form['email']
    }
    mysql.query_db(query, data)

    print("*"*50);
    print("User Updated! Redirecting . . .")

    return redirect("/users/{}".format(user_id))

@app.route("/users/<user_id>/destroy")
def delete_user(user_id):
    print("*"*50);
    print("Deleting user. . .");

    mysql = connectToMySQL("users")
    query = "DELETE FROM friends WHERE idfriends = %(id)s"
    data = {
        "id" : user_id
    }
    user = mysql.query_db(query, data)
    
    print("*"*50);
    print("User Deleted! Redirecting . . .");

    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)