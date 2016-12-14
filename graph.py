

class Graph:

	def __init__(self):
		self.adjacency_matrix = []
		self.incidence_matrix = []

	#Permet de charger un graphe à partir d'un fichier
	def load(self, uri):
		with open(uri, 'r') as file:
			#Loop on each line of the file in format 1,2,3,4 and map it into list of int [1,2,3,4]
			self.adjacency_matrix = [list(map(int, line.rstrip('\n').split(','))) for line in file]

	#Sauvegarde le graphe construit dans un fichier
	def save(self, uri):
		with open(uri, 'w') as file:
			for line in testList:
				#Convert list of int in string and add \n
				file.write(','.join(str(e) for e in line) + '\n')

		#Building the incidence matrix
		stopI = 0
		appendArray = []

		for lineI, line in enumerate(adjacency_matrix): 
			#Adding new array for incidence
			self.incidence_matrix.append(appendArray)
			stopI += 1

			for valI, val in enumerate(line[:stopI]):
				if val != 0:
					appendArray.append(0)
					for incidenceI, line in enumerate(self.incidence_matrix):
						#Adding correct value in incidence
						if incidenceI == valI or incidenceI == lineI:
							line.append(val)
						else:
							line.append(0)

	#Ajouter un noeud dans un graphe. 
	#Param : La ligne de matrice d'adjacence à ajouter.
	def addNode(self, n_adjacency):
		line_size = len(self.adjacency_matrix)+1

		if len(n_adjacency) != line_size:
			raise ValueError('Too much/not enough adjacency value')

		i = 0
		for elem in self.adjacency_matrix:
			elem.append(n_adjacency[i])
			i += 1

		self.adjacency_matrix.append(n_adjacency)

		#Adding to incidence
		#Init new incidence line
		try:
			newA = []
			for i in self.incidence_matrix[0]:
				newA.append(0)
		except IndexError:
			newA = []

		#Adding value in incidence line
		for valI, val in enumerate(n_adjacency):
			if val != 0:
				newA.append(val)
				for i, l in enumerate(self.incidence_matrix):

					if i == valI:
						l.append(val)
					else:
						l.append(0)
		#Adding new line to incidence
		self.incidence_matrix.append(newA)

	#Allow to remove a specific node of the graphe
	def removeNode(self, indice):
		if indice < 0 or indice > len(self.adjacency_matrix):
			raise ValueError("Index out of bound")
		self.adjacency_matrix.pop(indice)

		for l in self.adjacency_matrix:
			l.pop(indice)

		#Remove from incidence
		r = self.incidence_matrix.pop(indice)

		for i, l in enumerate(r):
			if l != 0:
				for line in self.incidence_matrix:
					line.pop(i)

	#Build the incidence matrix
	def getIncidence(self):
		return self.incidence_matrix

	#Floor the adjacence matrix to remove negative weight
	#def getFlooredAdjacence():

	#Floor the incidence matrix to remove negative weight
	#def getFlooredIncidence():
	def printIncidence(self):
		return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.incidence_matrix])

	def __str__(self):
		return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.adjacency_matrix])


