//A sample person model
const mongoose = require('mongoose'); //import and save db to const
//establish schema and save to const
const PersonSchema = new mongoose.Schema({
    firstName: { type: String },
    lastName: { type: String }
}, { timestamps: true });
//export
module.exports = mongoose.model('Person', PersonSchema);