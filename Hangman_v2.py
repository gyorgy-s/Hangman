import random
import os
import ascii_art
import word_list

# Clear the console dependeng on the OS
def clear():
 
    # for windows
    if os.name == 'nt':
        os.system('cls')
 
    # For mac and linux(here, os.name is 'posix').
    else:
        os.system('clear')

# Get a random word from word_list.py, and generate the blank string accordingly.
word_hidden = list(random.choice(word_list.list))
word_shown = list("_" * len(word_hidden))

choice = ""

life = 6

clear()

print(ascii_art.logo)

print("{0} ".format("  ".join(word_shown)))

# while the user has lives, keep asking for an input, which should be a alphabetical charater, the match that input to the characters of the chosen word. If the characers match, replace the corresponding blank in "word_hidden" to the character. If there is no match, decrease the number of lives, and print the corresponding ascii art. Then repeat.
while life > 0:
    if "_" in word_shown:

        while len(choice)!=1 or not choice.isalpha():
            choice = input("Guess a letter: ").lower()
            
        if word_hidden.count(choice):       #alternate condition: if choice is not in word_hidden:
            for i in range(len(word_hidden)):
                if choice == word_hidden[i]:
                    word_shown[i] = choice
        else :
            life -= 1  

        choice = ""
        clear()
        print(ascii_art.logo)
        print("{0} ".format("  ".join(word_shown)))
        print(ascii_art.stages[life])
        print("Life remaining:", life)
    
    else:
        print("You won!")
        exit()

print("You lose!")
