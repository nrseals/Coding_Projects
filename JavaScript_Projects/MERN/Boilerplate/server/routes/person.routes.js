const PersonController = require('../controllers/person.controller');  //Import
module.exports = (app) => {
    //begin routes
    app.get('/api', PersonController.index);
    app.post('/api/people', PersonController.createPerson);
}

