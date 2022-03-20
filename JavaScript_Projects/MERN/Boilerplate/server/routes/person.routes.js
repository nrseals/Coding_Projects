const PersonController = require('../controllers/person.controller');  //Import
module.exports = (app) => {
    app.get('/api', PersonController.index);
}

