#import random library for the computer to choose the number
import random
print("If you want to quit, type quit.")
runner_code=True
while runner_code:
    print("Computer chose a number in the range 0-10")
    computer_guess=random.randint(0,10)
    print("Do you wanna guess what it is?")
    user_input=input("User Guess: ")
    if user_input!='quit':
        user_input=int(user_input)
        if user_input==computer_guess:
            print("Victory!!!")
            print("User guess",user_input)
            print("computer guess",computer_guess)
            print("____________________________________________________________________________")
        else:
            print("Try again!")
            print("User guess",user_input)
            print("computer guess",computer_guess)
            print("____________________________________________________________________________")
            if user_input>10 or user_input<0:
                print("Choose number in the range again.")
    if type(user_input)==str and user_input=='quit':
        print("Quit")
        runner_code=False