# Bank Class 
class Bank:
    account={
        "acc":[101,102,103,104],
        "pin":[1111,2222,3333,4444],
        "bal":[1000,2000,3000,4000]
    }
    def __init__(self,acc,pin,bal):
        self.acc=acc
        self.pin=pin
        self.bal=bal
        print("Login Successfully")
        self.showMenu()
    # Function for checking balance

    def showBal(self):
        for i in range(4):
            pin=input("Enter pin: ")
            if pin==self.account["pin"][self.account["acc"].index(self.acc)]:
                print("Total Balance: ",self.account["bal"][self.account["acc"].index(self.acc)])
                self.showMenu()
            else:
                    print("You entered wrong pin")
                    print("Only ",3-i,"attempts left")

    def showMenu(self):
        print("-----Welcome to Bank-----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Reset pin")
        print("5. Self Transfer")
        print("6. Transfer to Other Account")
        print("7. Logout")
        choice=int(input("Enter YOur choice: "))
        if choice == 1 :
            self.showBal()
        elif choice ==2:
            self.deposit()
        elif choice == 3 :
            self.withdraw()
        elif choice == 4 :
            self.resetPin()
        elif choice == 5 :
            self.selfTransfer()
        elif choice == 6 :
            self.transfertoOtherAccount()
        elif choice == 7 :
            self.logOut()
        else:
            print("Invalid Choice")
            self.showMenu()
    # function for Deposit Money
    def deposit(self):
        amt=input("ENter amount to deposit: ")
        pin=int(input("Enter pin: "))
        if pin==self.account["pin"][self.account["acc"].index(self.acc)]:
            self.account["bal"][self]

    # function for Withdraw Money
    def withdraw(self):
        amt=input("ENter amount to withdraw: ")
        pin=int(input("Enter pin: "))
        if pin==self.account["pin"][self.account["acc"].index(self.acc)]:
            if int(amt)<=self.account["bal"][self.account["acc"].index(self.acc)]:
                self.account["bal"][self.account["acc"].index(self.acc)]-=int(amt)
                print("Withdraw Successfully")
                print("Total Balance: ",self.account["bal"][self.account["acc"].index(self.acc)])
                self.showMenu()
            else:
                print("Insufficient Balance")
                self.showMenu()
    # function for Reset Pin
    def resetPin(self):
        pin=int(input("Enter old pin: "))
        if pin==self.account["pin"][self.account["acc"].index(self.acc)]:
            newPin=int(input("Enter new pin: "))
            self.account["pin"][self.account["acc"].index(self.acc)]=newPin
            print("Pin Reset Successfully")
            self.showMenu()
        else:
            print("You entered wrong pin")
            self.showMenu()

    # function for Self Transfer
    def selfTransfer(self):
        amt=input("ENter amount to transfer: ")
        pin=int(input("Enter pin: "))
        if pin==self.account["pin"][self.account["acc"].index(self.acc)]:
            if int(amt)<=self.account["bal"][self.account["acc"].index(self.acc)]:
                self.account["bal"][self.account["acc"].index(self.acc)]-=int(amt)
                print("Transfer Successfully")
                print("Total Balance: ",self.account["bal"][self.account["acc"].index(self.acc)])
                self.showMenu()
            else:
                print("Insufficient Balance")
                self.showMenu()

    # function for Transfer to Other Account 
    def transfertoOtherAccount(self):
        pass

    # function for LogOut
    def logOut(self):
        pass

b1=Bank(101,1111,1000)