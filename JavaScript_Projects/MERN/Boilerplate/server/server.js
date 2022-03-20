//package imports
const express = require('express');
const cors = require('cors'); 


const app = express(); //sets up server
app.use(cors()); //Allows for cross origin requests
app.use(express.json());  //allows JSON objects to be posted
app.use(express.urlencoded({ extended: true })); //Allows json objects with strings and arrays

require('./config/mongoose.config');//import mongoose config
require('./routes/person.routes')(app);   // We're importing the routes export. 
// These two lines are the long-hand notation of the code above. They better show what's going on.
    // const personRoutes = require("./routes/person.routes"); <-- assign the exported function to a const
    // personRoutes(app); <-- invoke the function and pass in the express "app" server

app.listen(8000, () => {
    console.log("Listening at Port 8000")
})

