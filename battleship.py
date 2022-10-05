class Map:
	grid_size = 10
	empty_symbol = ' '
	boat_symbol = 'x'

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
			if input() == '':
				return False
			return True

		def add_boat(i):
			def get_orientation():
				print("To place the boat horizontaly enter h, to place it verticaly enter v")
				orientation = input().lower()
				if orientation != 'h' and orientation != 'v':
					self.print_grid()
					print("Incorrect input")
					orientation = get_orientation()
				return orientation

			def remove_boat():
				self.print_grid()
				for coordinate in self.boats.pop(-1):
					self.grid[coordinate['y']][coordinate['x']] = self.empty_symbol

			def get_user_input():
				self.print_grid()
				print("Placing a {} of size {} ".format(boat_name, boat_size), end='')
				if orientation == 'v': print("verticaly")
				else: print("horizontaly")

				user_input = Input()
				# Below is not grid_size - 1 as the boat starts on current index
				if (orientation == 'v' and user_input.y + boat_size > self.grid_size) \
					or (orientation == 'h' and user_input.x + boat_size > self.grid_size):
					print("The boat is too big to be placed here")
					return get_user_input()
				return user_input

			def append_boat_to_boats(boat_size):
				self.boats.append([])
				while boat_size > 0:
					# - 1 in both case as the boat starts on user_input.x/y not after
					if orientation == 'h':
						self.boats[-1].append({'y': user_input.y, 'x': user_input.x + boat_size - 1})
					else:
						self.boats[-1].append({'y': user_input.y + boat_size - 1, 'x': user_input.x})
					boat_size -= 1

			def write_boad_on_grid():
				for coordinate in self.boats[-1]:
					self.grid[coordinate['y']][coordinate['x']] = self.boat_symbol

			if i > 0 and cancel_last_placement():
				remove_boat()
				return i - 1

			self.print_grid()
			print("Placing a {name} of size {size}".format(name=boat_name, size=boat_size))
			orientation = get_orientation()
			user_input = get_user_input()
			append_boat_to_boats(boat_size)
			write_boad_on_grid()

		boats_to_add = [
			[5, "Carrier"],
			[4, "Battleship"],
			[3, "Destroyer"],
			[3, "Submarine"],
			[2, "Patrol Boat"]
		]
		i = 0
		while i < len(boats_to_add):
			boat_size = boats_to_add[i][0]
			boat_name = boats_to_add[i][1]
			i = add_boat(i)
			if i == len(boats_to_add) - 1 and cancel_last_placement(): i -= 1


	def print_grid(self):
		print("     A   B   C   D   E   F   G   H   I   J")
		print("   -----------------------------------------")
		for i in range(len(self.grid)):
			if i > 8:
				print(i + 1, end=' ')
			else:
				print(" {} ".format(i + 1), end='')
			for square in self.grid[i]:
				print("| {} ".format(square), end='')
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

		if type(letter) == int: return letter
		return availible_letters.find(letter)

	def get_y(self, call):
		print("Pick y coordinates (number)")
		number = input()

		if len(number) == 0 or number.upper() not in "1, 2, 3, 4, 5, 6, 7, 8, 9, 10":
			print("Coordinates should be a number between 1 and 10")
			number = self.get_y(1)

		if call > 0: return number
		return int(number) - 1
