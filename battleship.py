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
