#number_guesser_game

import random
logo="""                                                                            
                       | |                                                    
  _ __  _   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___  ___ _ __ 
 | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __|/ _ \ '__|
 | | | | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \  __/ |   
 |_| |_|\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/\___|_|   
                                           __/ |                              
                                          |___/                               
"""
print(logo)
condition=True

#chances of each
easytrial=10
moderatetrial=7
hardtrial=5
NUMBER=(random.randrange(0,200,1))

#defining comparator
def comparator(num):
    if((NUMBER//2)<num<NUMBER):
        print(f"guessed number is {num} which is low from the number to be guessed")
    elif((NUMBER+NUMBER//2)>num>NUMBER):
        print(f"guessed number is {num} which is high from the number to be guessed")
    elif(num<NUMBER):
        print(f"guessed number is {num} which is too low from the number to be guessed")
    elif(num>NUMBER):
        print(f"guessed number is {num} which is too high from the number to be guessed")
    else:
        print(f"you have guessed correctly the number to be guessed was {NUMBER}")

#actual asker and counting tries
def game_actuall(trial):
    n=0
    while(n<trial):
        number1=int(input("\nGuess a number -->"))
        comparator(number1)
        if(number1!=NUMBER):
            print(f"{trial-(n+1)} guesses left")
            n+=1 
        else:
            break
    if(n==trial):
        print(f"\nout of chances the number was {NUMBER}")

#various modes
#easy mode
def easy():
    print(f"difficulty mode selected is easy so the number of chances to guess the number is {easytrial}")
    game_actuall(easytrial)
#moderate mode
def moderate():
    print(f"difficulty mode selected is moderate so the number of chances to guess the number is {moderatetrial}")
    game_actuall(moderatetrial)
#hard mode
def hard():
    print(f"difficulty mode selected is hard so the number of chances to guess the number is {hardtrial}")
    game_actuall(hardtrial)

#actually main code to do work
def code():
    mode=(input("\nWhich difficulty mode would you like to choose easy, moderate, hard -->").lower())
    if(mode == "easy"):
        easy()
    elif(mode == "moderate"):
        moderate()
    elif(mode == "hard"):
        hard()
    else:
        print("Enter valid difficulty mode")

#base structure main code
#initial ask
play=(input("Do you want to play the game (yes/no) -->").lower())
if(play=="yes"):
    condition1=True
    while(condition1):
        code()
        again=input("Do you want to play again (yes/no)-->").lower()
        if(again=="yes"):
            condition1=True
            print("Game loaded again")
            code()
        else:
            print("\nThankyou for visiting the number guesser game")
            condition1=False
else:
    print("Thankyou for visiting")

