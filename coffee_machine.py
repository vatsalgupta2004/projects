# menu list
#coffee machine
logo=""" 
   _____  ____   ______  ______  ______  ______     __  __            _____  _    _  _____  _   _  ______ 
  / ____|/ __ \ |  ____||  ____||  ____||  ____|   |  \/  |    /\    / ____|| |  | ||_   _|| \ | ||  ____|
 | |    | |  | || |__   | |__   | |__   | |__      | \  / |   /  \  | |     | |__| |  | |  |  \| || |__   
 | |    | |  | ||  __|  |  __|  |  __|  |  __|     | |\/| |  / /\ \ | |     |  __  |  | |  | . ` ||  __|  
 | |____| |__| || |     | |     | |____ | |____    | |  | | / ____ \| |____ | |  | | _| |_ | |\  || |____ 
  \_____|\____/ |_|     |_|     |______||______|   |_|  |_|/_/    \_\._____||_|  |_||_____||_| \_||______|
"""
def reciept1(coffee2,remaining_change):
    logo1 = f"""
    —————————————————————————————————————————————
         item                  price            
    _____________________________________________
    {coffee2}               ${(MENU[coffee2]["cost"])}                
    _____________________________________________                    
            your change amount -->${remaining_change}         
        "thankyou for visting cafe high town"      
    ___________________._________________________
    """
    print(logo1)

print(logo)

start=((input("click start/stop to operate the coffee machine accordingly -->")).lower())
if(start == "start"):
    MENU = {
        "espresso":
            {
                "ingredients":
                    {
                        "water": 50,
                        "milk": 0,
                        "coffee": 18,
                    },
                "cost": 1.5,
            },
        "latte":
            {
                "ingredients":
                    {
                        "water": 200,
                        "milk": 150,
                        "coffee": 24,
                    },
                "cost": 2.5,
            },
        "cappuccino":
            {
                "ingredients":
                    {
                        "water": 250,
                        "milk": 100,
                        "coffee": 24,
                    },
                "cost": 3.0,
            },
        }

    # resources
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    total_sale = 0

    # coins
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    condition = True
    while (condition):
        #type of coffee
        def types_coffee(coffee2):
            global resources
            global total_sale
            if(resources["water"]>(MENU[coffee2]["ingredients"]["water"])):
                if(resources["milk"]>(MENU[coffee2]["ingredients"]["milk"])):
                    if(resources["coffee"]>(MENU[coffee2]["ingredients"]["coffee"])):

                        print(f"\nso it would be ${MENU[coffee2]["cost"]} for 1 {coffee2}")
                        print("please insert coins")
                        quarters1 = int(input("No of quarters (.25$) -->"))
                        dimes1 = int(input("No of dimes (.10$) -->"))
                        nickles1 = int(input("No of nickles (.05$) -->"))
                        pennies1 = int(input("No of pennies (.01$) -->"))
                        total_cost = ((quarters * quarters1) + (dimes * dimes1) + (nickles * nickles1) + (pennies * pennies1))

                        if (total_cost >= (MENU[coffee2]["cost"])):
                            for item in resources :
                                resources[item] -= (MENU[coffee2]["ingredients"][item])

                            total_sale += (MENU[coffee2]["cost"])
                            print(f"\nhere is your {coffee2} ☕ enjoy")
                            print("Have a nice day")
                            remaining_change = round((total_cost - (MENU[coffee2]["cost"])),2)
                            print(f"your remaining change is ${round(remaining_change,2)}\n")
                            print("\n here's your reciept -->")
                            reciept1(coffee2,remaining_change)

                        else:
                            print("sorry that's not enough money")
                            print(f"money refunded")
                    else:
                        print("sorry insufficient ingredients please contact the staff")
                else:
                    print("sorry insufficient ingredients please contact the staff")
            else:
                print("sorry insufficient ingredients please contact the staff")

    #main code
        coffee1 = (input("\nWhat would you like to have (espresso/latte/cappuccino) -->").lower())

        if (coffee1 == "report"):
            print("\nmachine report -->")
            print(f"water : {resources["water"]}ml \nmilk : {resources["milk"]}mg\ncoffee : {resources["coffee"]}mg\nsales : ${total_sale}")

        elif (coffee1 == "espresso"):
            types_coffee(coffee1)

        elif (coffee1 == "latte"):
            types_coffee(coffee1)

        elif (coffee1 == "cappuccino"):
            types_coffee(coffee1)

        elif (coffee1 == "off"):
            resources = {
                "water": 300,
                "milk": 200,
                "coffee": 100,
            }
            total_sale = 0
            print("system off and can be reseted now")
            print("system after reset -->")
            print(f"water :{resources["water"]}\nmilk :{resources["milk"]}\ncoffee :{resources["coffee"]}\nsales :{total_sale}")
else:
    print("Coffee machine stopped run the program again to start the machine")
    print("Have a nice day")

