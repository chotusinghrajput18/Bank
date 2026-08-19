# Bank Class 
class Bank:
    def __init__(self,acc,pin,bal):
        self.acc=acc
        self.pin=pin
        self.bal=bal
        print("Login Successfully")
    # Function for checking balance
    def showBal(self):
        pin=input("Enter pin: ")
        if pin==self.pin:
            print("Total Bal: ",self.bal)
        else:
            print("You entered wrong pin")
b1=Bank(101,1111,1000)
b1.showBal()