# File: CS112_A1_T2_Game2_20230584.py
"""
Purpose: Number scrabble is a game that played within a list of numbers from 1:9 Each player takes turns picking a
number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers
that add up to 15, that player wins the game. However, if all the numbers are used and no player gets exactly 15,
the game is a draw.
"""


# Author: Malak Reda Mohamed Esmail
# ID: 20230584

# start the game
def start_the_game():
    # set list of numbers
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1 = 0
    player2 = 0

    # welcome message and display status
    print("Welcome to Number Scrabble Game")
# game playing 
    # making a loop 
    for _ in range(0,5):
        print("The list of numbers:", numbers_list)
        player1 += player_turn(1, numbers_list)
        if player1 == 15:
            print("Player 1 is the winner")
            return
        print("The list of numbers:", numbers_list)
        player2 += player_turn(2, numbers_list)
        if player2 == 15:
            print("Player 2 is the winner")
            return

    print("All numbers are used and the game is a draw.")


def player_turn(numbers_list):
    while True:
        try:
            picked_number = int(input("Player 1 : Please pick a number from the list: "))
            if picked_number in numbers_list:
                numbers_list.remove(picked_number)
                return picked_number
            else:
                print("Wrong number. Player 1 : Please enter a number from the list.")
        except ValueError:
            print("Incorrect input. Player 1 : Please enter a valid number.")
    while True:
        try:
            picked_number = int(input("Player 2 : Please pick a number from the list: "))
            if picked_number in numbers_list:
                numbers_list.remove(picked_number)
                return picked_number
            else:
                print("Wrong number. Player 2:  Please enter a number from the list.")
        except ValueError:
            print("Incorrect input. Player 2 : Please enter a valid number.")

start_the_game()
