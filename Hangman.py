import random
import os


def clear():
 
    # for windows
    if os.name == 'nt':
        os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

word_list = ["ardvark", "baboon", "camel"]

word_hidden = list(random.choice(word_list))
word_shown = list("_" * len(word_hidden))

choice = ""

print("{0} ".format("  ".join(word_shown)))

cond = "".join(word_shown)

life = 5
while life > 0:
    if not cond.isalpha():
        while len(choice)!=1 or not choice.isalpha():
            choice = input("Guess a letter: ").lower()
        if word_hidden.count(choice):
            for i in range(len(word_hidden)):
                if choice == word_hidden[i]:
                    word_shown[i] = choice
        else :
            life -= 1        
        choice = ""
        clear()
        cond = "".join(word_shown)
        print("{0} ".format("  ".join(word_shown)))
        print("Life remaining:", life)
    else:
        print("You won!")
        exit()
print("You lose!")
