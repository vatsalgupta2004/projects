import random
from project3.hangmanimports import logo
from project3.hangmanimports import word_list
from project3.hangmanimports import stages

play_again=True
while(play_again):

  print(logo)
  print("welcome to the hangman word guessing game \nsave the man from hanging by guessing the correct word\n")
  random_word=random.choice(word_list)

  guessedword=[]
  for i in range(0,len(random_word),1):
      guessedword.append("⬜️")
  #print(f"choosen word is {random_word}")

  lives=6
  end_of_game=True
  while (end_of_game):

      choosen_word=input("guess a letter : ").lower()
      for j in range(0,len(random_word),1):

          if(random_word[j]==choosen_word):
              guessedword[j]=choosen_word

      if(choosen_word in guessedword):
          print(f"the word {choosen_word} already guessed")

      else:
        if (choosen_word not in random_word):
            lives-=1
            print(stages[lives])
            print(f"you gussed the letter '{choosen_word}' which is not in the word\nyou lose a life")
            print(f"{lives} lives are left")
            if (lives == 0):
                end_of_game=False
                print(f"\nthe word was '{random_word}'")
                print("GAME OVER! YOU LOST ALL YOUR LIVES")

      print(f"\n{' '.join(guessedword)}")

      if "⬜️" not in guessedword:
          end_of_game = False
          print("GAME OVER! YOU WON YOU GUESSED THE RIGHT WORD")
        
  condition=input("do you want to play again yes or no :").lower()
  if (condition=="no"):
      print("thankyou for playing")
      play_again=False
  
  else:
      play_again=True