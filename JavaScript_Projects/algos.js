function lastOfAToTheB(a, b) {
    let c = 1;
    for (let i = 1; i <= b; i++){
        c *= a;
    }
    return (c % 10);
}
// console.log(lastOfAToTheB(3, 4)) //returns 1
// console.log(lastOfAToTheB(12, 5))//returns 2

function statToDouble(){
    //set up dice function
    function rollDie(){
        return Math.ceil(Math.random()*6);
    }
    //initialize stat values
    let rolls = 0;
    let sum = 0;
    let avg = 0;
    let min = 12;
    let max = 2;
    while(avg == 0){
        //create pair of dice
        let d1 = rollDie();
        let d2 = rollDie();
        console.log(`Roll 1 is ${d1}, Roll 2 is ${d2}`);
        let pair = d1 + d2
        //incriment rolls
        rolls ++;
        //continuously adds sum of the pair of dice to value stored in sum, used to find avg
        sum += pair;
        //compare sum of two dice to min, if less than, set min to sum
        if(min > pair){
            min = pair;
        }
        //compare sum of two dice to max, if greater than, set max to sum
        if(max < pair){
            max = pair;
        }
        //if d1 and d2 are the same, calculate the average, ending the loop and log results to the console
        if(d1 == d2){
            avg = Math.floor(sum /rolls);
            console.log(`DOUBLE! The min is ${min}, the max is ${max}, the dice were rolled ${rolls} times, the average sum of the dice was ${avg}`)
        }
    }
}
statToDouble();
