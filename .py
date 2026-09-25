class practice:
    n=1
    def __init__(self):
        print("you are now eligible for registration.")
        self.dashboard()
    def dashboard(self):
        print("1- Registration")
    def registration(self):
        while self.n!=0:
            name=input("Enter your name: ")
            if name.isalpha():
                phone=int(input("Enter phone no.: " ))
                if len(phone)==10:
                    email=input("Enter your email: ")
                    if email.isalnum():
                        pass
                    else:
                        continue
                else:
                    continue
            else:
                continue
            