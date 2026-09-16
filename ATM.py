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