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
    // transferMoney(otherUser, amount) {
    //     this.accountBalance -= amount;
    //     otherUser.accountBalance += amount;
    //     console.log("************");
    //     console.log(`Transfered $${amount} from ${this.name} to ${otherUser.name}`)
    //     return this
    // }
}



//test cases
// const checking = new BankAccount("checking",0.1, 1000);
// const savings = new BankAccount("savings", 0.2, 5000)

// checking.deposit(100).deposit(500).deposit(100).withdrawal(200).yeildInterest().displayBalance()

// savings.deposit(1000).deposit(1000).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).yeildInterest().displayBalance()

class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
        this.account = new BankAccount(intRate = 0.2, balance = 0)//using parameter names allows us to input them out of order
    }
    createAccount(name) {
        const newAcc = new BankAccount(name = name)
        console.log("*********")
        console.log(`Created new account ${name} for ${this.name}`)
    }
    makeDeposit(amount) {
        this.account.name.deposit(amount);
    }
    makeWithdrawal(amount) {
        this.account.withdrawal(amount);
    }
    displayUserBalance(){
        this.account.displayBalance();
    }
}
const nathan = new User("Nathan", "seals@mail.com")