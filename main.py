
from graph import Graph

G = Graph()
G.addNode([0])

print(G)

G.addNode([1,0])
print(G)

G.addNode([0,1,0])
print(G)

print(G.getIncidence())

G.removeNode(0)
print(G)
print(G.getIncidence())

G.load("test.gr")
print(G)
print(G.getIncidence())
