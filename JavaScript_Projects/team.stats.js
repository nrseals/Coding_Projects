const team = {
    _players: [{
      firstName:'Nathan',
      lastName: 'Seals',
      age: 30},
      {firstName: 'Tonya',
      lastName: 'Harding',
      age: 23},
      {firstName: 'Tyler',
      lastName: 'Evans',
      age: 26}],
    _games: [{
      opponent: 'Carolina Crown',
      teamPoints: 95,
      opponentPoints: 99},
      {opponnent: 'Blue Devils',
      teamPoints: 99,
      opponentPoints: 89},
      {opponent: 'Bluecoats',
      teamPoints: 89,
      opponentPoints: 97}],
    get players() {
      return this._players;
    },
    get games() {
      return this._games;
    },
   addPlayer(firstName, lastName, age){
      let newPlayer = {
        firstName: firstName,
        lastName: lastName,
        age: age
      }
      this.players.push(newPlayer);
      console.log(`${firstName} ${lastName} added to team!`)
    },
  addGame(opponentName, teamPoints, opponentPoints){
    let newGame = {
      opponentName: opponentName,
      teamPoints: teamPoints,
      opponentPoints: opponentPoints
    }
    this.games.push(newGame);
    console.log(`Game versus ${opponentName} added!`);
  
  }
  }
    team.addPlayer('Steph','Curry', 28);
    team.addPlayer('Lisa', 'Leslie', 44);
    team.addPlayer('Bugs', 'Bunny', 76);
    // console.log(team._players);
    team.addGame('The Cadets', 98, 88);
    team.addGame('The Cavliers', 88, 90);
    team.addGame('Santa Clara Vanguard', 90, 95);
    // console.log(team._games)