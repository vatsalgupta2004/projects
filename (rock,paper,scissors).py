condition=True
while(condition==True):
    rock = '''
        _______
    ---'    ____)
           (_____)
           (_____)
           (____)
    ---.__(___)
    '''

    paper = '''
         _______
    ---'   _____)
             _____)
             _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ___)_____
            ________)
           __________)
          (____)
    ---.__(___)
    '''
    import random
    print("hello this program is specially designed to play the game rock🪨, paper📃 and scissors✂️  with you\n")
    choice=int(input("please enter your choice from the following options\nrock : 1\npaper : 2\nscissors : 3\n=>"))
    choice -=1
    if(choice==0 or choice==1 or choice==2):
        selection_random=random.randint(0,2)
        choose=["rock","paper","scissors"]
        option=[rock,paper,scissors]

        if(selection_random==0 and choice==0):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"both sides have chosen same MATCH DRAW!")

        elif(selection_random==0 and choice==1):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"YOU WON!")

        elif(selection_random==0 and choice==2):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"YOU LOST!")
        #2 when program chooses paper or 1
        if(selection_random==1 and choice==0):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"YOU LOST!")

        elif(selection_random==1 and choice==1):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"MATCH DRAW!")

        elif(selection_random==1 and choice==2):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"YOU WON!")

        #3 when program chooses scissors or 2
        if(selection_random==2 and choice==0):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"YOU WON!")

        elif(selection_random==2 and choice==1):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"YOU LOST!")

        elif(selection_random==2 and choice==2):
            print(f"program choose {choose[selection_random]}")
            print(option[selection_random])
            print(f"you choose {choose[choice]}")
            print(option[choice])
            print(f"MATCH DRAW")

        play_again=input("do you want to play again yes or no :")
        print(" ")
        if(play_again=="yes"):
            condition=True
        else:
            condition=False
            print("Thankyou for visiting the program and i hope you had fun playing the game")

    else:
        print("enter valid value from the given options\n")
        