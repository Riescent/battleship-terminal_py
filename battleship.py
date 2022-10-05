class Map:
    grid_size = 10
    empty_symbol = " "
    boat_symbol = "x"

    def __init__(self):
        self.grid = []
        for y in range(self.grid_size):
            self.grid.append([])
            for x in range(self.grid_size):
                self.grid[y].append(self.empty_symbol)
        self.boats = []
        self.add_boats()

    def add_boats(self):
        def cancel_last_placement():
            print("To continue: press enter. To cancel: type anything")
            if input() == "":
                return False
            return True

        def remove_boat():
            self.print_grid()
            for index in self.boats.pop(-1):
                self.grid[index["y"]][index["x"]] = self.empty_symbol

        def add_boat(boat_size, boat_name, i):
            def get_orientation():
                print("To place the boat horizontaly enter h")
                print("To place it verticaly enter v")
                orientation = input().lower()
                if orientation != "h" and orientation != "v":
                    self.print_grid()
                    print("Incorrect input")
                    orientation = get_orientation()
                return orientation

            def get_user_input():
                def boat_is_on_the_way():
                    for add_me in range(boat_size):
                        if (
                            orientation == "h"
                            and self.grid[user_input.y][user_input.x + add_me]
                            == self.boat_symbol
                        ):
                            return True
                        elif (
                            orientation == "v"
                            and self.grid[user_input.y + add_me][user_input.x]
                            == self.boat_symbol
                        ):
                            return True

                self.print_grid()
                print("Placing a {} of size {} ".format(boat_name, boat_size), end="")
                if orientation == "v":
                    print("verticaly")
                else:
                    print("horizontaly")

                user_input = Input()
                # Below is not grid_size -1 as the boat starts on current index
                if (
                    orientation == "v" and user_input.y + boat_size > self.grid_size
                ) or (orientation == "h" and user_input.x + boat_size > self.grid_size):
                    return 1
                if boat_is_on_the_way():
                    return 2
                return user_input

            def append_boat_to_boats():
                self.boats.append([])
                for add_me in range(boat_size):
                    if orientation == "h":
                        self.boats[-1].append(
                            {"y": user_input.y, "x": user_input.x + add_me}
                        )
                    else:
                        self.boats[-1].append(
                            {"y": user_input.y + add_me, "x": user_input.x}
                        )

            def write_boat_on_grid():
                for index in self.boats[-1]:
                    self.grid[index["y"]][index["x"]] = self.boat_symbol

            self.print_grid()
            if i > 0:
                if cancel_last_placement():
                    remove_boat()
                    return i - 1
                self.print_grid()

            print("Placing a {} of size {}".format(boat_name, boat_size))
            orientation = get_orientation()
            user_input = get_user_input()
            while type(user_input) != Input:
                self.print_grid()
                if user_input == 1:
                    print("The boat is too big to be placed here")
                else:
                    print("There is another boat on the way")
                orientation = get_orientation()
                user_input = get_user_input()

            append_boat_to_boats()
            write_boat_on_grid()
            return i + 1

        boats_to_add = [  # [i][0] == size, [i][1] == name
            [5, "Carrier"],
            [4, "Battleship"],
            [3, "Destroyer"],
            [3, "Submarine"],
            [2, "Patrol Boat"],
        ]
        i = 0
        while i < len(boats_to_add):
            i = add_boat(boats_to_add[i][0], boats_to_add[i][1], i)
            if i == len(boats_to_add):
                self.print_grid()
                if cancel_last_placement():
                    remove_boat()
                    i -= 1

    def print_grid(self):
        print("     A   B   C   D   E   F   G   H   I   J")
        print("   -----------------------------------------")
        for i in range(len(self.grid)):
            if i > 8:
                print(i + 1, end=" ")
            else:
                print(" {} ".format(i + 1), end="")
            for square in self.grid[i]:
                print("| {} ".format(square), end="")
            print("|\n   -----------------------------------------")


class Input:
    def __init__(self):
        self.y = self.get_y(0)
        self.x = self.get_x()

    def __repr__(self):
        return "Input: y == {y}, x == {x}".format(y=self.y, x=self.x)

    def get_x(self):
        print("Pick x coordinates (letter)")
        letter = input().upper()

        availible_letters = "ABCDEFGHIJ"
        if len(letter) != 1 or letter not in availible_letters:
            print("Coordinates should be a letter between A and J")
            letter = self.get_x()

        if type(letter) == int:
            return letter
        return availible_letters.find(letter)

    def get_y(self, call):
        print("Pick y coordinates (number)")
        number = input()

        if len(number) == 0 or number.upper() not in "1,2,3,4,5,6,7,8,9,10":
            print("Coordinates should be a number between 1 and 10")
            number = self.get_y(1)

        if call > 0:
            return number
        return int(number) - 1
