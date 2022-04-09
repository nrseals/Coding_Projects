//package imports
const express = require('express');
const cors = require('cors'); 


const app = express(); //sets up server
app.use(cors()); //Allows for cross origin requests
app.use(express.json());  //allows JSON objects to be posted
app.use(express.urlencoded({ extended: true })); //Allows json objects with strings and arrays

require('./config/mongoose.config');//import mongoose config
require('./routes/item.routes')(app);  //import routes


app.listen(8000, () => {
    console.log("Listening at Port 8000")
})

