# PIG

import random

"""
program that allows players (2-4) to play in every turn and they have to throw a dice
They one who reached 50 first won, else the one who has max score more that 50 wins... but if there
is a player who throws 1 as a dice, this will reset the count to 0
"""

print("******************")
print("**** PIG GAME ****")
print("******************")
print("\n")


def roll():
    min_value =1
    max_value = 6

    randon_value = random.randint(min_value, max_value)

    return randon_value


while True:
    player = input("Pick a number between 2-4 for the number of players to play: ")


    if player.isdigit():
        player = int(player)

        if player <= 2 or player <=4:
            print(f"\n number of player selected : {player}")
            break
        else:
            print("Mininum 2 players and maximum 4 players ")
            continue

    else:
        print("Invalid Choice")


players = [0 for _ in range(player)]

current_score = 0

max_score =50

while max(players) < max_score:

    for player_index in range(player):


            print(f"\nTurn of player {player_index + 1}")
            print(f"score: {players[player_index]}")

            while current_score !=1:

                play = input("Do you wanna roll ? (Y) :").lower()

                while play != 'y':
                     print("Incorrect input")
                     play = input("Do you wanna roll ? (Y) :").lower()

                current_score = roll()
                if current_score != 1:

                    print(f"You have rolled {current_score}")
                    players[player_index] += current_score
                    print(f"total : {players[player_index]}")



            current_score = 0
            print("You have rolled 1!!!!, Turn done")

            print(f"\nPlayer {player_index + 1}, score: {players[player_index]}")





max_score = max(players)

winner = players.index(max_score)

print(f"\nPlayer number {winner + 1} is the winner with the score {max_score}")

