//Controller import
const ItemController = require('../controllers/item.controller');  
module.exports = (app) => {
    //begin routes
    app.get('/api', ItemController.index);
    app.post('/api/items', ItemController.createItem);
    //can be the same route as POST as long as we have a different http verb
    app.get('/api/items', ItemController.getAllItems); 
}

