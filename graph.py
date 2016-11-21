

class Graph:

	def __init__(self):
		self.adjacency_matrix = []

	def load(self, uri):
		with open(uri, 'r') as file:
			#Loop on each line of the file in format 1,2,3,4 and map it into list of int [1,2,3,4]
			self.adjacency_matrix = [list(map(int, line.rstrip('\n').split(','))) for line in file]

	def save(self, uri):
		with open(uri, 'w') as file:
			for line in testList:
				#Convert list of int in string and add \n
				file.write(','.join(str(e) for e in line) + '\n')

	def addNode(self, n_adjacency):
		line_size = len(self.adjacency_matrix)+1

		if len(n_adjacency) != line_size:
			raise ValueError('Too much/not enough adjacency value')

		i = 0
		for elem in self.adjacency_matrix:
			elem.append(n_adjacency[i])
			i += 1

		self.adjacency_matrix.append(n_adjacency)

	def removeNode(self, indice):
		if indice < 0 or indice > len(self.adjacency_matrix):
			raise ValueError("Index out of bound")
		self.adjacency_matrix.pop(indice)

		for l in self.adjacency_matrix:
			l.pop(indice)

	def __str__(self):
		return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.adjacency_matrix])


