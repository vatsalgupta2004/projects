#caeser cipher problem
logo ="""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88                                   
                                                         
           00             88
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
condition = True
while (condition):

    direction = input("Enter whether to encrypt/encode or decrypt/decode :")
    text = (input("Enter the text you want to encrypt :")).lower()
    shift = int(input("Enter the number of shifts you desire :")) 

    def encrypt(text1,shift1):
        cipher_text=""
        for letter in text1 :
            if(letter not in alphabet):
                cipher_text+=letter
            else:
                position = alphabet.index(letter)
                new_position = (position + shift1)
                if(new_position>25):
                    new_position = (new_position % 26)
                new_letter = alphabet[new_position]
                cipher_text += new_letter
        print(f"encoded text is {cipher_text}")

    def decrypt(text2,shift2):
        cipher_text_decrypted=""
        for letter in text2:
            if(letter not in alphabet):
                cipher_text_decrypted+=letter
            else:
                position = alphabet.index(letter)
                new_position = (position - shift2)
                if(new_position <0):
                    new_position = (new_position % 26)
                new_letter = alphabet[new_position]
                cipher_text_decrypted += new_letter
        print(f"decoded text is {cipher_text_decrypted}")

    if (direction == "encode" or direction == "encrypt"):
        encrypt(text,shift)
    elif (direction == "decode" or direction == "decrypt"):
        decrypt(text,shift)
    else :
        print("enter valid option and run again")

    condition1=(input("Do you want to continue encrypting or decrypting the text (yes/no):")).lower()
    
    if (condition1 == "yes"):
        condition = True
    else:
        condition = False
        print("Thankyou for visiting the caeser cipher problem")


     