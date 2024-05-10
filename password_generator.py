letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','?']

import random

print("This pyhton program helps you to create a strong password of desired length\n")

letters_num=int(input("How many letter would you want in your password ?\n:"))
numbers_num=int(input("How many digits would you want in your password ?\n:"))
symbols_num=int(input("How many symbols would you want in your password ?\n:"))

letterlist=[]
for i in range(0,letters_num):
    letterlist.append(random.choice(letters))

numberlist=[]
for j in range(0,numbers_num):
    numberlist.append(random.choice(numbers))

symbollist=[]
for k in range(0,symbols_num):
    numberlist.append(random.choice(symbols))

password=(letterlist+numberlist+symbollist)
#print(password)
final_pass=random.sample(password,len(password))#random.sample -> returns a list with randomised elements but no of elements to be returned must be specified
#print(final_pass)
password_2=""
for l in final_pass:
    password_2+=l
print(f"Here is your password : {password_2}")