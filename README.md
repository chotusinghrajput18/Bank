class Bank:
    def __init__(self,acc,pin,bal):
        self.acc=acc
        self.pin=pin
        self.bal=bal
    def showBal(self):
        pin=intput("Enter your pin:")
        if pin==self.pin:
            print("Bal: ₹",self.bal)
        else:
            print("Wrong pin")