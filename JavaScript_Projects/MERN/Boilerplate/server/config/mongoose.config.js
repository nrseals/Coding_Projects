const mongoose = require('mongoose');
//This will create a database named "person" if one doesn't already exist (no need for mongo shell!):
const dbName = "*INSERT DB NAME HERE*";
mongoose.connect("mongodb://localhost/crmdb", { 
    useNewUrlParser: true, 
    useUnifiedTopology: true,
})
    .then(() => console.log(`Established a connection to the database ${dbName}`))
    .catch(err => console.log("Something went wrong when connecting to the database", err));

