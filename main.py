# File: bakjg001_my_wordle.py
# Author: Jirah Baker
# Student ID: 110332584
# Email ID: bakjg001
# Description: Assignment 2 - My Wordle!
# This is my own work as defined by the UniSA's Academic Misconduct policy.

import random


# Function definition for displaying the personal details to the screen
def display_details():

    # Print statements to display the details to the screen
    print("File: bakjg001_converter.py")
    print("Author: Jirah Baker")
    print("Student ID: 110332584")
    print("Email ID: bakjg001")
    print("Description: Assignment 2 - My Wordle")
    print("This is my own work as defined by the UniSA's Academic Misconduct policy.")
    return None


def get_wordle_guess (word_list, attempt):

    user_guess = input("Please enter your guess - attempt " + str(attempt) + ": ")

    in_the_list = 0

    while len(user_guess) != 5 or in_the_list == 0:

        index = 0

        while index < len(word_list):
            if user_guess == word_list[index]:
                in_the_list = 1
            index = index + 1

        if len(user_guess) != 5:
            print("Five letter words only please.")
            user_guess = input("Please enter your guess - attempt " + str(attempt) + ": ")
        elif in_the_list == 0:
            print("Not in word list!")
            user_guess = input("Please enter your guess - attempt " + str(attempt) + ": ")

        user_guess = user_guess

    return user_guess


def create_word_list(filename):

    infile = open(filename, "r")

    word_list = infile.readline().split(" ")

    infile.close()
    
    return word_list


word_list = create_word_list("word_file.txt")

print("---------------------------------")
print("--         My Wordle!          --")
print("-- Guess the Wordle in 6 tries --")
print("---------------------------------")

playing = input("\nWould you like to play My Wordle [y|n]? ")

while playing != 'y' and playing != 'n':
    playing = input("Would you like to play My Wordle [y|n]? ")

while playing == 'y':
    wordle = random.choice(word_list)

    correct_letters = ""
    used_letters = ""
    hat_string = " "
    dummy_wordle = list(wordle)

    print("Wordle is:", wordle)

    print("-------------")
    print("| - - - - - |")

    guess_1 = get_wordle_guess(word_list, 1)

    print("You guessed:",guess_1)

    print("-------------")
    print("|", guess_1[0], guess_1[1], guess_1[2], guess_1[3], guess_1[4], "|")
    
    index = 0
    while index < len(guess_1):
        if guess_1[index] == wordle[index]:
            correct_letters = correct_letters + guess_1[index]
            hat_string = hat_string + "^ "
            dummy_wordle[index] = "-"
        else:
            hat_string = hat_string + "- "
        index = index + 1

    hat_list = list(hat_string)

    index = 0

    while index < len(guess_1):
        if guess_1[index] in dummy_wordle:
            used_letters = used_letters + guess_1[index]
            hat_list[index] = "*"
            dummy_wordle[index] = "-"
        index = index + 1

    print("".join(hat_list))
    print(hat_list)
    print(hat_string)
    print(dummy_wordle)
    print(used_letters)

    playing = input("\nWould you like to play again [y|n]? ")

    while playing != 'y' and playing != 'n':
        playing = input("\nWould you like to play again [y|n]? ")


print("Thanks for playing!")