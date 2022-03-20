const PersonController = require('../controllers/person.controller');  //Import
module.exports = (app) => {
    //begin routes
    app.get('/api', PersonController.index);
    app.post('/api/people', PersonController.createPerson);
    app.get('/api/people', PersonController.getAllPeople); 
    //can be the same route as POST as long as we have a different http verb
}

