#higher lower guesser game
import random
logo = """
/=======================================================================================\.
|  _     _       _                 _                                                     |
| | |   (_)     | |               | |                                                    |
| | |__  _  __ _| |__   ___ _ __  | | _____      _____ _ __    __ _ _   _  ___  ___ ___  |
| | '_ \| |/ _` | '_ \ / _ \ '__| | |/ _ \ \ /\ / / _ \ '__|  / _` | | | |/ _ \/ __/ __| |
| | | | | | (_| | | | |  __/ |    | | (_) \ V  V /  __/ |    | (_| | |_| |  __/\__ \__ \.|
| |_| |_|_|\__, |_| |_|\___|_|    |_|\___/ \_/\_/ \___|_|     \__, |\__,_|\___||___/___/ |
|           __/ |                                              __/ |                     |
|          |___/                                              |___/                      |
\=======================================================================================/.
"""

logo2 = """ 
 __      _______ 
 \ \    / / ____|
  \ \  / / (___  
   \ \/ / \___ \ 
    \  /  ____) |
     \/  |_____/ 
"""
print(logo)

def names(names):
    print(f"Name -->{names}\nDescription -->{followers_description[names]["description"]}")#\nFollowers -->{followers_description[names]["followers"]}")

scorecount=0

play=(input("Do you want to play the higher lower guess game (yes/no) -->").lower())
if(play == "yes"):
    list_name = ["virat kohli","the beatles","cristiano ronaldo","jake paul","narendra modi","priyanka chopra","kylie jenner","lionel messi"]
    followers_description={"virat kohli":
                            {"description":"famous indian cricket player",
                            "followers":268,
                            },
                            "the beatles":
                            {"description":"famous american band",
                                "followers":5,
                            },
                            "cristiano ronaldo":
                            {"description":"famous portugal origin football player",
                                "followers":629,
                            },
                            "jake paul":
                            {"description":"famous american content creator",
                                "followers":27,
                            },
                            "narendra modi":
                            {"description":"famous indian politician",
                                "followers":89,
                            },
                            "priyanka chopra":
                            {"description":"famous indian actress",
                                "followers":91,
                            },
                            "kylie jenner":
                            {"description":"famous american model",
                                "followers":400,
                            },
                            "lionel messi":
                            {"description":"famous argentina origin football player",
                                "followers":503,
                            },
                            }
    
    condition = True
    while(condition):
        print("\nOption --> A")
        name1 = (random.choice(list_name))
        names(name1)

        print(logo2)

        print("\nOption --> B")
        name2 = (random.choice(list_name))
        sametest = True
        while(sametest):
            if(name2 == name1):
                name2 = (random.choice(list_name))
                if(name2 == name1):
                    sametest = True
                else:
                    sametest = False
            else:
                sametest = False
        names(name2)

        print(" ")

        def comparator(name1f,name2f):
            global scorecount
            global condition
            if(followers_description[name1f]["followers"]>followers_description[name2f]["followers"]):
                print(f"Your guess option {guess.upper()} is correct")
                scorecount=scorecount+1
                print(f"Your score is {scorecount}")
            else:
                print(f"You guess option {guess} is incorrect")
                print(f"Your final score is {scorecount}")
                again = (input("\nDo you want to play agian (yes/no) -->").lower())
                if(again == "yes"):
                    condition = True
                    scorecount=0
                else:
                    condition = False
                    print("Thakyou for visiting the game")

        guess=(input("Guess who has more followers A or B -->"))
        if(guess == "a" or guess == "A"):
            comparator(name1f=name1,name2f=name2)

            # scorecount = 0
            # if(followers_description[name1]["followers"]>followers_description[name2]["followers"]):
            #     print(f"Your guess option {guess} is correct")
            #     scorecount+=1
            #     print(f"Your score is {scorecount}")
            # else:
            #     print(f"You guess option {guess} is incorrect")
            #     print(f"Your score is {scorecount}")
            #     again = (input("Do you want to play agian (yes/no) -->").lower())
            #     if(again == "yes"):
            #         condition = True
            #     else:
            #         condition = False
            #         print("Thakyou for visiting the game")

        elif(guess == "b" or guess == "B"):
            comparator(name1f=name2,name2f=name1)

            # def comparator(name1f,name2f):
            #     scorecount = 0
            #     if(followers_description[name2]["followers"]>followers_description[name1]["followers"]):
            #         print(f"Your guess option {guess} is correct")
            #         scorecount+=1
            #         print(f"Your score is {scorecount}")
            #     else:
            #         print(f"You guess option {guess} is incorrect")
            #         print(f"Your score is {scorecount}")
            #         again = (input("Do you want to play agian (yes/no) -->").lower())
            #         if(again == "yes"):
            #             condition = True
            #         else:
            #             condition = False
            #             print("Thakyou for visiting the game")

else:
    print("\nThankyou for visting the game")