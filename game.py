import os  # Used to clear the terminal using os.system("clear||cls")
from battleship import *


def clear_terminal():
    os.system("clear||cls")


class Player:
    def __init__(self):
        print("Input player name")
        self.name = input()
        # TODO check if player name is empty
        print("{} choose where to put your boats".format(self.name))
        self.map = Map()
        clear_terminal()


def win(player_name):
    print("\n{} won the game, congratulations!\n".format(player_name))


def press_enter_to_continue(clear_terminal_after_enter=True):
    print("Press enter to continue...")
    input()
    if clear_terminal_after_enter:
        clear_terminal()


def call_next_player(player):
    clear_terminal()
    print("Stop looking at the screen and call for {}".format(player))
    press_enter_to_continue()


def play(player, enemy):
    def print_grids():
        clear_terminal()
        players[enemy].map.print_grid(players[enemy].map.shoot_grid)
        print(players[enemy].name)
        players[player].map.print_grid(players[player].map.grid)
        print(players[player].name)

    print_grids()
    print("{} attacks {}".format(players[player].name, players[enemy].name))
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
