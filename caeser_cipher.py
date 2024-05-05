from project3.caeser_cipher_art import logo
#caeser cipher problem
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


     