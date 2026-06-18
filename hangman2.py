import random

var_hang = ["""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
        |
        |
        |
        |
=============""","""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
    0   |
        |
        |
        |
=============""","""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
    0   |
    |   |
        |
        |
=============""","""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
    0   |
   /|\  |
        |
        |
=============""","""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
=============""","""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
    0   |
   /|\  |
   /|   |
        |
=============""","""
HANGMAN GAME - Vegetables Edition
    +---+
    |   |
    0   |
   /|\  |
   /|\  |
        |
============="""]
def func_RandomWord():
    var_words=['carrot','broccoli','corn','cucumber','lettuce','mushrooms','onion',
               'potato','cabbage','pumpkin','tomato','beetroot','peas','radish','leek',
               'celery','eggplant']
    var_word=random.choice(var_words)
    return var_word

def func_displayB(var_hang, var_missedLet, var_correctLet, var_sWord):
    print(var_hang[len(var_missedLet)])
    print()
    print('Missed Letter:', end=' ')
    for letter in var_missedLet:
        print(letter, end=' ')
    print("\n")
    blanks='_'*len(var_sWord)
    for i in range(len(var_sWord)):
        if var_sWord[i] in var_correctLet:
            blanks=blanks[:i]+var_sWord[i]+blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print("\n")

def func_guess(alreadyGuessed):
    while True:
        var_guess = input("Guess a letter: ")
        var_guess = var_guess.lower()
        if len(var_guess) != 1:
            print("Please enter only single letter.")
        elif var_guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif var_guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return var_guess

def func_playAgain():
    return input("Do you want to play again? (y/n)").lower().startswith('y')

var_missedLet = ''
var_correctLet = ''
var_sWord = func_RandomWord()
var_gameComp = False

while True:
    func_displayB(var_hang, var_missedLet, var_correctLet, var_sWord)
    var_guess = func_guess(var_missedLet + var_correctLet)
    if var_guess in var_sWord:
        var_correctLet += var_guess
        foundAllLetters = True
        for i in range(len(var_sWord)):
            if var_sWord[i] not in var_correctLet:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes!! The secret word is ' + var_sWord + ' You have WON!!!')
            var_gameComp = True
    else:
        var_missedLet += var_guess
        if len(var_missedLet) == len(var_hang) - 1:
            func_displayB(var_hang, var_missedLet, var_correctLet, var_sWord)
            print("You have run out of guesses! After: " + str(len(var_missedLet)) + ' missed guesses and ' + str(len(var_correctLet)) + ' correct guesses, the word was "' + var_sWord + '".')
            var_gameComp = True
    if var_gameComp:
        if func_playAgain():
            var_missedLet = ''
            var_correctLet = ''
            var_gameComp = False
            var_sWord = func_RandomWord()
        else:
            break
