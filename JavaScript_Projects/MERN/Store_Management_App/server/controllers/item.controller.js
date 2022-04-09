
// set up controllers based on classes 

const Item = require('../models/item.model');
// test function
module.exports.index = (request, response) => {
    response.json({
        message: "Hello World"
    });
}
//create 
module.exports.createItem = (request, response) => {
    //Mongoose create function
    Item.create(request.body)
        .then(item => response.json(item))
        .catch(err => response.json(err));
}
//display all
module.exports.getAllItems = (request, response) => {
    // Mongoose find function
    Item.find({})
        .then(all_items => {
            console.log(all_items);
            response.json(all_items);
        })
        .catch(err => {
            console.log(err)
            response.json(err)
        })
}
