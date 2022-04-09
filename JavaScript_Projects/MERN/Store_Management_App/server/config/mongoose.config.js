//Mongoose import
const mongoose = require('mongoose');

const dbName = "store_db";
//Mongoose connect function
mongoose.connect("mongodb://localhost/crmdb", { 
    useNewUrlParser: true, 
    useUnifiedTopology: true,
})
    .then(() => console.log(`Established a connection to the database ${dbName}`))
    .catch(err => console.log("Something went wrong when connecting to the database", err));

