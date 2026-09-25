class Practice:
    n=1
    def __init__(self):
        print("you are now eligible for registration.")
        self.dashboard()
    def dashboard(self):
        print("1- Registration")
        ch=int(input("Enter a choice: "))
        if ch==1:
            self.registration()
    def registration(self):
        while self.n>0:
            name=input("Enter your name: ")
            if name.isalpha():
                while self.n>0:
                    phone=input("Enter phone no.: " )
                    if len(phone)==10 and phone.isalnum():
                        while self.n>0:
                            email=input("Enter your email: ")
                            if '@' in email and len(email)>8:
                                print("Registration successfull ")
                                self.n=0
                                break
                            else:
                                print("invalid input")
                                continue
                    else:
                        print("invalid phone")
                        continue
                else:
                    print("Invalid name")
                    continue
p=Practice()