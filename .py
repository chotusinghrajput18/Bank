import pygame
import random
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
        elif ch==2:
            self.guestlogin()
        
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
                                self.home()
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
    def snakeGame(self):
        # pygame.init()
        # self.red=(255,0,0)
        # self.blue=(100,153,150)
        # self.grey=(192,192,192)
        # self.green=(51,102,0)
        # self.yellow=(0,255,255)
        # self.win_width=600
        # self.win_height=400
        # self.window=pygame.display.set_mode((self.win_width,self.win_height))
        # pygame.display.set_caption("Snake Game")
        pass
    def guestLogin(self,id=0000,password=0000):
        self.showGuestMenu()
    def showGuestMenu(self):
        print("----- GAME SECTION -----")
        print("1- Snake Game")
        print("2- Word Guessing Game")
        print("3- LogOut")
        ch=int(input("Enter choice: "))
        if ch==1:
            self.snakeGame()
    


    def home(self):
        pass
p=Practice()