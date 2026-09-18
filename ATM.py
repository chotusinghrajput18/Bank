class ATM:
    Accounts={
        "acc":[123456, 234567, 345678, 456789],
        "pin":[1234, 2345, 3456, 4567],
        "bal":[1000, 2000, 3000, 4000]
    }
    def __init__(self, balance=100):
        self.balance= balance
        self.acc= self.Accounts["acc"]
        self.balance= self.Accounts["bal"]
    def login(self, acc, pin):
        if acc in self.acc:
            index= self.acc.index(acc)
            if pin==self.Accounts["pin"][index]:
                print("You are Logged in Successfully")
                self.showMenu(acc)
            else:
                print("Invalid Pin")
    def showMenu(self, acc):
        print("Welcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer to others acc")
        print("5. Reset Pin")
        print("6. Creating new Account")
    def checkBalance(self, acc):
        index= self.acc.index(acc)
        print("Your balance is: ", self.Accounts["bal"][index])
    def deposit(self, acc, amount):
        index= self.acc.index(acc)
        self.Accounts["bal"][index]+= amount
        print("Deposit Successful. New balance is: ", self.Accounts["bal"][index])
    def withdraw(self, acc, amount):
        index= self.acc.index(acc)
        if self.Accounts["bal"][index]>= amount:
            self.Accounts["bal"][index]-= amount
            print("Withdrawal Successful. New balance is: ", self.Accounts["bal"][index])
        else:
            print("Insufficient Balance")
    def transfer(self, acc, to_acc, amount):
        index= self.acc.index(acc)
        if self.Accounts["bal"][index]>= amount:
            if to_acc in self.acc:
                to_index= self.acc.index(to_acc)
                self.Accounts["bal"][index]-= amount
                self.Accounts["bal"][to_index]+= amount
                print("Transfer Successful. New balance is: ", self.Accounts["bal"][index])
            else:
                print("Invalid Account Number")
        else:
            print("Insufficient Balance")
    def resetPin(self, acc, old_pin, new_pin):
        index= self.acc.index(acc)
        if old_pin==self.Accounts["pin"][index]:
            self.Accounts["pin"][index]= new_pin
            print("Pin Reset Successful")
        else:
            print("Invalid Old Pin")