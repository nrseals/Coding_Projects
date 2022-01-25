
class BankAccount {
    constructor(name, intRate) {   
        this.name = name
        this.int = intRate
        this.balance = 0
    }
    deposit(amount) {
        this.balance += amount;
        console.log("************");
        console.log(`Deposited $${amount} to ${this.name}`)
        return this //Allows for methods to be chained. 
    }
    withdrawal(amount) {
        if ((this.balance - amount) < 0) {
            console.log("***********");
            console.log("Insufficient Funds! Cannot complete transaction")
        } else {
            this.blance -= amount;
            console.log("***********");
            console.log(`Withdrew $${amount} from ${this.name}`)
        }
        return this
    }
    displayBalance() {
        console.log("************");
        console.log(`The account balance for ${this.name} is $${this.balance}`)
        return this
    }
    yeildInterest(){
        const int = this.balance * this.int
        console.log("********")
        console.log(`The yieled interest for ${this.name} is $${int}`)
        return this
    }
}
export default BankAccount;
