
import re
""" Add loop trough word to show same letters and check if msg is a letter"""


def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))


def is_word(word):
    if re.match("^[a-zA-Z]+$", word):
        return True
    return False


word = input("Enter word: ").lower()
if is_word(word):

    hangman(word)
else:
    word = input("Enter word: ")
