print( '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |                  |
|___________________|__"=._o`"-._        `"=.______________|__________________|
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |                  |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|__________________|
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |                  |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|__________________|
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("Welcome to Treasure Island Your mission is to find the treasure")
path_choose=input("well now there are two paths left and right choose any one of them wisely :")
if(path_choose=="left"):
    next_step=input("oh you got through the first level but now choose either to wait or swim the river :")
    if (next_step=="wait"):
        final_stage=input("this is the last stage there are three magical doors red, yellow, and blue choose wisely and all the treasure is yours :")
        if(final_stage=="red"):
            print("Burned by fire Game Over 💀")
        elif(final_stage=="blue"):
            print("Eaten by beasts Game Over 💀")
        elif(final_stage=="yellow"):
            print("congratulations you have won the game and the treasure is all yours 🪙🪙🪙🪙")
        else:
            print("Game Over 💀")
    else:
        print("you are attacked by trout Game Over 💀")   
else:
    print("oh you fall into a hole Game Over💀")
print("thank you for playing play again soon")