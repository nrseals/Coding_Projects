from flask import Flask, jsonify
import json
from flask_cors import CORS
from config.mysqlconnection import connectToMySQL
app = Flask(__name__)
CORS(app)
# Begin routes
SCHEMA = "solo_project"

# Get items
@app.route("/items")
# simple route that returns JSON object, this will later be replaced with data from DB
def getitems():
    items = {"items": ["item 1", "item 2", "item 3"]}
    db = connectToMySQL(SCHEMA)
    gigsArray = db.query_db("SELECT name FROM gigs ORDER BY date ASC")
    # SQL query returns array of objects
    print(gigsArray)
    # next block of code uses for loop to extract names from objects, and push them into a new array, then the array of name is assigned to a new dictonary with the key "gigs"
    newArr = []
    for object in gigsArray:
        newArr.append(object['name'])
    gigs = {
        "gigs": newArr
    }
    print(gigs)
    return gigs
    


if __name__ == "__main__":
    app.run(debug=True)
