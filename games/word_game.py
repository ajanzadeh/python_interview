# Create a game where the computer picks a random word and the player has to guess that word. The
# computer tells the player how many letters are in the word. Then the player gets five chances to ask if a
# letter is in the word. The computer can only respond with "yes" or "no". Then, the player must guess the
# word

import random
def game():


    winner = False
    words = ["apple", "orranges", "ship", "war", "summer"]
    word = random.choice(words)
    print(word)
    print("the word has",len(word),"charechters")

    for i in range(1, 5):
        guess = input("guess\n")

        if guess == word:
            print("you won")
            winner = True
            break
        else:
            print("try again")
    if winner:
        print("I am happy for you, please try again")
    else: print("sorry, hope you try your chance again")
    
game()
