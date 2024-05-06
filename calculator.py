#calculator
logo = """
 _____________________
|  _________________  |
| | calculator      | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | * | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

"""
print(logo)

def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def divide(num1,num2):
    return(num1/num2)
def multiply(num1,num2):
    return(num1*num2)
def modulus(num1,num2):
    return(num1%num2)
def exponent(num1,num2):
    return(num1**num2)

operations={"+":add,"-":sub,"/":divide,"*":multiply,"%":modulus,"**":exponent}

def calculator():
    
    num1=int(input("Enter first number :"))
    for item in operations:
        print(item)
    
    condition = True
    while(condition):
        
        operation_symbol=input("Enter the operation symbol you want to perform :")
        num2=int(input("Enter next nummber :"))
        
        if(operation_symbol=="/" and num2 == 0):
            print("invalid dividing by 0 results in undefined value")
            condition2=input("Do you want to start calculations again -->(yes/no) :").lower()
            if(condition2=="yes"):
                calculator()
            else:
                print("Thankyou for visiting")
                condition=False
        else:
            calculation_func=operations[operation_symbol]
            answer=calculation_func(num1,num2)
            
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            
            continue1=input("Do you want to continue the calculations (yes/no) or run again (again) :").lower()
            
            if(continue1 == "yes"):
                num1=calculation_func(num1,num2)
            elif(continue1 == "again"):
                condition=True
                print("\nCalculator program running again -->")
                calculator()
            else:
                condition = False
                print("Thank you visiting the calculator program")
calculator()

    