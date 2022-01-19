class School {
    constructor(name, level, numberOfStudents){
      //super refers to this
      this._name = name;
      this._level = level;
      this._numberOfStudents = numberOfStudents;
    }
    get name() {
      return this._name;
    }
    get level() { 
      return this._level;
    }
    get numberOfStudents() {
      return this._numberOfStudents;
    }
    set numberOfStudents(newNumberOfStudents){
      if(typeof newNumberOfStudents === 'number'){
        this.numberOfStudents = newNumberOfStudents;
      } else {
        console.log('Invalid input: numberOfStudents must be set to a number')
      }
    }
    quickFacts(){
      console.log(`${this.name} educates ${this.numberOfStudents} students at the ${this.level} level.`);
    }
    static pickSubstituteTeacher(substituteTeachers){
      let randomNum = Math.floor(Math.random() * substituteTeachers.length);
      // console.log(randomNum);
      // console.log(substituteTeachers[randomNum]);
      return substituteTeachers[randomNum];
    }
  }
  class PrimarySchool extends School{
    //does not need to take in level arg
    constructor(name,numberOfStudents, pickupPolicy){
      //refers to original school object
      super(name, 'primary',numberOfStudents);
      this._pickupPolicy = pickupPolicy;
    }
    get pickupPolicy(){
      return this._pickupPolicy;
    }
  }
  class HighSchool extends School {
    constructor(name, numberOfStudents, sportsTeams){
      super(name, 'high', numberOfStudents);
      this._sportsTeams = sportsTeams;
      }
      get sportsTeams(){
        console.log(sportsTeams);
      }
  }
  const lorraineHansbury = new PrimarySchool(name = 'Lorrane Hansbury', numberOfStudents = 514, pickupPolicy = 'Students must be picked up by a parent, guardian, or a family member over the age of 13.');
  // console.log(lorraineHansbury)
  lorraineHansbury.quickFacts();
  School.pickSubstituteTeacher(['Jamal Crawford', 'Lou Williams', 'J. R. Smith', 'James Harden', 'Jason Terry', 'Manu Ginobli'])
  const alSmith = new HighSchool ('Al E. Smith', 415, ['Baseball', 'Basketball', 'Volleyball', 'Track and Field'])
  // alSmith.quickFacts()
  console.log(alSmith._sportsTeams)
  