const getUserChoice = userInput => {
    userInput = userInput.toLowerCase();
    if (userInput === "rock" || userInput === 'paper' || userInput === 'scissors' || userInput === "bomb"){
      // console.log(`Success userInput is ${userInput}`)
      return userInput;
    } else {
      console.log("Error with userInput");
    }
  }
  //Test for getUserChoice
  // getUserChoice('scissors');
  // getUserChoice('death');
  const getComputerChoice = () =>{
    n = Math.floor(Math.random()*3);
    if(n === 0){
      // console.log(`Number is ${n}. Computer Choice is rock`);
      return 'rock';
      } else if (n === 1) {
        // console.log(`Number is ${n}. Computer Choice is paper`)
        return 'paper'
      } else if (n===2) {
        // console.log(`Number is ${n}. Computer choice is scissors`);
        return 'scissors';
      }
    }
    // Tests for getComputerChoice();
  // getComputerChoice();
  // getComputerChoice();
  // getComputerChoice();
  determineWinner = (userChoice, computerChoice) => {
    if (userChoice === computerChoice){
      return 'tie';
    }
    if (userChoice === 'bomb'){
      return 'User wins'
    }
    if (userChoice === 'rock'){
      if(computerChoice === 'paper'){
        return "Computer wins"
      }else{
        return "User wins"
      }
    }
    if (userChoice === 'paper'){
      if(computerChoice === 'scissors'){
        return "Computer wins"
      } else {
        return "Computer wins"
      }
    }
    if (userChoice === 'scissors'){
      if(computerChoice === 'paper'){
        return "Computer wins"
      } else {
        return "User wins"
      }
    }
  }
  // Test for determineWinner
  // console.log(determineWinner(getUserChoice("scissors"),getComputerChoice()));
  const playGame = userInput => {
    let userChoice = getUserChoice(userInput);
    let computerChoice = getComputerChoice();
    console.log(`user chooses ${userChoice}`);
    console.log(`computer chooses ${computerChoice}`);
    let winner = determineWinner(userChoice, computerChoice);
    console.log(winner);
    return winner;
  }
  playGame('scissors')
  playGame('rock')
  playGame('paper')
  playGame('bomb')
  