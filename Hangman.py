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
choices = []

message = ""

life = 6

clear()

print(ascii_art.logo)
print("{0} ".format("  ".join(word_shown)))

# while the user has lives, keep asking for an input, which should be a alphabetical charater, the match that input to the characters of the chosen word. If the characers match, replace the corresponding blank in "word_hidden" to the character. If there is no match, decrease the number of lives, and print the corresponding ascii art. Then repeat.
# Additional message, if the chosen letter is or is not in the word, and store and check if the letter was guessed before.
while life > 0:
    if "_" in word_shown:
        choice = ""

        while len(choice)!=1 or not choice.isalpha():
            choice = input("Guess a letter: ").lower()
            
        if word_hidden.count(choice):       #alternate condition: if choice is not in word_hidden:
            if choice in choices:
                message = f"you've already tried \"{choice}\", it's in the word."
            else:
                choices.append(choice)
                message = f"it's in the word"
                for i in range(len(word_hidden)):
                    if choice == word_hidden[i]:
                        word_shown[i] = choice
        else :
            if choice in choices:
                message = f"you've already tried \"{choice}\", it's not in the word."
            else:
                choices.append(choice)
                message = f"it's not in the word"
                life -= 1  
        
        
        clear()
        
        print(ascii_art.logo)
        # print(word_hidden)
        
        print("{0} ".format("  ".join(word_shown)))
        
        print(ascii_art.stages[life])
        print(f"You've guessed \"{choice}\", " + message)
        print("Life remaining:", life)
    
    else:
        print("You won!")
        exit()

print("You lose!")
