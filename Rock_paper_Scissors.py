import random
user_guess_count =0
computer_guess_count=0
option = ["rock", "paper", "scissors"]

while True:
    user_pick = input("What is your option: ").lower()
    if user_pick == "q":
        break
    computer_guess = random.randint(0,2)
    computer_pick = option[computer_guess]
    print("Computer Picked " + computer_pick)
    if user_pick == "rock" and computer_pick =="scissors":
        print("You won")
        user_guess_count +=1
    elif user_pick == "paper" and computer_pick =="rock":
        print("You won")
        user_guess_count +=1
    elif user_pick == "scissors" and computer_pick =="paper":
        print("You won")
        user_guess_count +=1 
    else:
        print("You Lost")
        computer_guess_count +=1
print("Your score is " + str(user_guess_count))
print("Computer Score is: " + str(computer_guess_count))
print("Caio and thankyou for playing ;) ")
        
