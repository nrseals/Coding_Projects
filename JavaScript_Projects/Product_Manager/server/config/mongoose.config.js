const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/crmdb',
{
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
    .then (() => console.log("established connection to the database!"))
    .catch(err => console.log("something went wrong when connecting to the database", err));