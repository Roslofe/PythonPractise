"""
Write a program that lets the user play rock, paper, scissors against the computer."""

import random

def choose():
    num = random.randint(1, 3)
    if num == 1:
        chosen = "rock"
    elif num == 2:
        chosen = "paper"
    else:
        chosen = "scissors"
    return chosen

def determineWinner(option1, option2):
    if (option1 == "rock" and option2 == "scissors") or (option2 == "rock" and option1 == "scissors"):
        winner = "Rock"
    elif (option1 == "scissors" and option2 == "paper") or (option2 == "scissors" and option1 == "paper"):
        winner = "Scissors"
    else:
        winner = "Paper"
    return winner

def game():
    computerChoise = choose()
    playerChoise = input("Please choose rock, paper, or scissors by writing it on your keyboard: ")
    if playerChoise != "rock" and playerChoise != "paper" and playerChoise != "scissors":
        print("That is not a valid option. Please choose again.")
        playerChoise = input("Please choose rock, paper, or scissors by writing it on your keyboard: ")
    print("The computer has chosen", computerChoise)
    if computerChoise == playerChoise:
        print("It's a tie, the game must be replayed to determine a winner.")
        game()
    else:
        winner = determineWinner(computerChoise, playerChoise)
        print(winner, "wins.")
    again = input("The game is now complete. Type yes if you wish to play again. ")
    if again == "yes":
        game()
    else: 
        print("Goodbye!")

print("Welcome to playing rock, paper, scissors!")
game()