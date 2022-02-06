import {BankAccount} from './bank_account';
class User {
    constructor(firstName, lastName, email, password){
        this.firstName = firstName;
        this.lastName  = lastName;
        this.email = email;
        this.password = password;
    }
    createAccount(name) {
        const newAcc = new BankAccount(name = name)
        console.log("*********")
        console.log(`Created new account ${name} for ${this.name}`)
        return this
    }
    makeDeposit(amount) {
        this.account.name.deposit(amount);
        return this
    }
    makeWithdrawal(amount) {
        this.account.withdrawal(amount);
        return this
    }
    displayUserBalance(){
        this.account.displayBalance();
        return this
    }
}
export default User;