#blackjack/21 game

def game():
    repeat=True
    while(repeat):

        import random
        choice1=[11,2,3,4,5,6,7,8,9,10,10,10,10]

        user_player=[]
        user_computer=[]

        #sum of list elements
        def sum(list1):
            sum=0
            for i in list1:
                sum+=i
            return sum

        #random elements picker
        def hit(user):
            user.append(random.choice(choice1))

        #comparator
        def comparator():
            if(user_computer_sum==user_player_sum):
                print(f"both have same {user_computer_sum} sum of cards therefore the game is tied")
            elif(user_player_sum>user_computer_sum):
                print(f"you won as the sum of your cards is {user_player_sum} which is greater than sum of computer's cards {user_computer_sum}")
            else:
                print(f"you lost as the sum of your cards is {user_player_sum} which is less than sum of computer's cards {user_computer_sum}")

        #user_player
        hit(user_player)
        hit(user_player)
        print(f"your cards are --> {user_player}")
        user_player_sum=sum(user_player)
        print(f"sum of your cards is --> {user_player_sum}\n")

        #user_computer
        hit(user_computer)
        hit(user_computer)
        print(f"computer's cards are --> {user_computer}")
        user_computer_sum=(sum(user_computer))
        print(f"sum of computer's cards is --> {user_computer_sum}\n")

        #further_code
        condition=True

        while(condition):
            if(user_player_sum<17):
                print("you have a sum less than 17 so hitting another card ")
                hit(user_player)
                print(f"your cards are --> {user_player}")
                user_player_sum=sum(user_player)
                print(f"sum of your cards is --> {user_player_sum}\n")
                condition=True
            else:
                condition=False

        if (user_player_sum>21):
            print(f"Sum of your cards is {user_player_sum} which is greater than 21")
            print("You lost")

        else:
            condition1=input("Do you want to hold with your cards or hit again (hit/hold) -->").lower()
            if(condition1=="hit"):
                hit(user_player)
                print(f"your cards are --> {user_player}")
                user_player_sum=sum(user_player)
                print(f"Sum of current cards is --> {user_player_sum}\n")
                
                if(user_player_sum>21):
                    
                    for i in range(0,len(user_player),1):
                        if(user_player[i] == 11):
                            user_player.insert(i,1)
                            user_player_sum=sum(user_player)
                        else:
                            print(f"you lost the game as the sum of your cards is {user_player_sum} which exceeded 21\n")
                            break
        
            elif(condition1=="hold"):
                print(f"\nso you are holding your current cards are --> {user_player}")
                print(f"sum of the cards you are holding currently is --> {user_player_sum}\n")
                
                condition2=True
                while(condition2):
                    if(user_computer_sum<17):
                        hit(user_computer)
                        print(f"computer's cards are --> {user_computer}")
                        user_computer_sum=sum(user_computer)
                        print(f"sum of computer's cards are --> {user_computer_sum}\n")
                        condition2=True
                    else:
                        condition2=False

                    if(user_computer_sum>21):
                        for i in range(0,len(user_computer),1):
                            if(user_computer[i] == 11):
                                user_computer.insert(i,1)
                                user_computer_sum=sum(user_computer)
                                comparator()
                            else:
                                print(f"computer lost the game as the sum of computer's cards is {user_computer_sum} which exceeded 21")
                                break
                    else:
                        comparator()
                        break
                # else:
                #     print("you lost")
                #     break
            else:
                print("enter valid option")
                break
        
        repeat1=input("\nDo you want to play again (yes/no) --> ").lower()
        if(repeat1=="yes"):
            print(" ")
            repeat=True
        else:
            print("Thankyou for playing the game 🃏")
            repeat=False

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
play=input("Do you want to play the blackjack game (yes/no) -->").lower()
if(play=="yes"):
    print("\nwelcome to the game\n")
    game()
else:
    print("Thankyou")

