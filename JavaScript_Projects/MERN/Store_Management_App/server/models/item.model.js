//import and save db to const
const mongoose = require('mongoose');

//create new instance of Mongoose Schema object
const ItemSchema = new mongoose.Schema({
    itemName: { type: String },
    department: { type: String },
    price: { type: Number },
    inStock: { type: Boolean, default: false },
    quantityInStock: { type: Number, default: 0 },
    location: { type: String, default: "A1" }
}, { required: ["itemName", "department", "price"] }, { timestamps: true });


//export model
module.exports = mongoose.model('Item', ItemSchema);