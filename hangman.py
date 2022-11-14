import random
import words.txt
points_initial = 10
HINT_LENGTH = 3

Letter = 1
WORD = 2
HINT = 3

_rand = random.Random()
play_again_request = False
def load_words(file='words.ext'):
    words = []
    f_words =open(file)
    for line in f_words:
        word = line.strip()
        if(word.isalpha()):
            words.append(line.strip())
    f_words.close()
    return words

def get_random_word(words_list):
    list_of_indexes = [i for i, j in enumerate(word) if j == letter]
    for index in list_of_indexes:
        pattern[index] = letter
    return _rand.choice(words_list)

def play_again():
    play_again = input("Do you want to play again? y = yes, n = no \n")
    while play_again not in ["y", "n", "Y", "N"]:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_again =="y":
        main()
    elif play_game =="n":
        print("Thank you for playing")
        exit()

def play_game
    global word()
    pattern = ["_" for _ in range(len(word))]
    while already_guessed == False
        if len(guess) == 1:
            if guess not in alphabet:
                print("wrong")
            elif guess in letters_guessed:
                print("You have already guessed that letter before.")
            elif guess not in word:
                print("Sorry, that ketter it not part of the word")
                letters_guessed.append(guess)
            elif guess in word:
                print("Great")
            else:
               print("Check your entry")
        elif len(guess) == len(word):
            if guess == word:
                print("great job!")
                guessed = True
            else:
                print("sorry,try again")
        else:
            print("sorry, try again")

