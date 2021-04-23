import random
from os import system 
def screen_clear():
    _=system('cls')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice="yes"
while choice=="yes":
    user_choice=int(input("Enter 0 for Rock, 1 for Paper, and 2 for Scissors: "))
    if user_choice>=3 or user_choice<0:
        print("You entered an invalid choice, YOU LOSE!!!")
    else:
        if(user_choice==0):
            print("You chose Rock")
            print(rock)
        elif(user_choice==1):
            print("You chose Paper")
            print(paper)
        elif (user_choice==2):
            print("You chose Scissors")
            print(scissors)
        choices=[rock,paper,scissors]
        length=len(choices)
        comp_choice=random.randint(0,length-1)
        if comp_choice==0:
            print("Computer chose Rock")
            print(rock)
        elif comp_choice==1:
            print("Computer chose Paper")
            print(paper)
        elif comp_choice==2:
            print("Computer chose Scissors")
            print(scissors)

        if user_choice==0 and comp_choice==2:
            print("YOU WIN!!!")
        elif comp_choice==0 and user_choice==2:
            print("YOU LOSE!!!")
        elif comp_choice>user_choice:
            print("YOU LOSE!!!")
        elif user_choice>comp_choice:
            print("You WIN!!!")
        elif(user_choice==comp_choice):
            print("It's a draw")
    choice=input("Do you want to play again? Type yes or no. ").lower()
    screen_clear()