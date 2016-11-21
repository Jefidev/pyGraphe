
from graph import Graph

G = Graph()
G.addNode([0])

print(G)

G.addNode([1,0])
print(G)

G.removeNode(0)
print(G)

G.load("test.gr")
print(G)
