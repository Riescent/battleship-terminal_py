class Map:
	def __init__(self):
		self.grid = [[' ' for x in range(10)] for y in range(10)]

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
