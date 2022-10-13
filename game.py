import os # Used to clear the terminal using os.system("clear||cls")
from battleship import *


def clear_terminal():
    os.system("clear||cls")


class Player:
    def __init__(self):
        self.name = input("Input player name: ")
        while self.name == "":
            self.name = input("Player name can't be empty\nInput player name: ")
        print(f"{self.name} choose where to put your boats")
        self.map = Map()
        clear_terminal()


def win(player_name):
    print(f"\n{player_name} won the game, congratulations!\n")


def press_enter_to_continue(clear_terminal_after_enter=True):
    input("Press enter to continue...")
    if clear_terminal_after_enter:
        clear_terminal()


def call_next_player(player):
    clear_terminal()
    print(f"Stop looking at the screen and call for {player}")
    press_enter_to_continue()


def play(player, enemy):
    def print_grids():
        clear_terminal()
        players[enemy].map.print_grid(players[enemy].map.shoot_grid)
        print(players[enemy].name)
        players[player].map.print_grid(players[player].map.grid)
        print(players[player].name)

    print_grids()
    print(f"{players[player].name} attacks {players[enemy].name}")
    players[enemy].map.get_shot_at()

    print_grids()

    if players[enemy].map.all_ships_are_destroyed():
        win(players[player].name)
        press_enter_to_continue(False)
        return True

    press_enter_to_continue()
    call_next_player(players[enemy].name)


clear_terminal()
print("Welcome to Battleship terminal py\n")

players = [Player(), Player()]

call_next_player(players[0].name)

while True:
    if play(0, 1):
        break
    if play(1, 0):
        break
