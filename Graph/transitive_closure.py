from collections import defaultdict

class Graph:

    def __init__(self, V):
       self.V = V

       self.graph = defaultdict(list)

       self.tc = [[0 for j in range(self.V)] for i in range(self.V)]


    def addEdge(self, u , v):
        self.graph[u].append(v)

    def dfsutil(self, a, b):

        self.tc[a][b] = 1

        for i in self.graph[b]:
            if self.tc[a][i]==0:
                self.dfsutil(a,i)

    def transitiveClosure(self):
        for i in range(self.V):
            self.dfsutil(i,i)

        print(self.tc)





edges = int(input("Enter the num of edges: "))
vertices = int(input("Enter the num of vertices: "))

g = Graph(vertices)
for z in range(0,edges):
    print("Input edge" , z+1)
    x=int(input("Enter edge starting node: "))
    y=int(input("Enter edge ending node: "))
    g.addEdge(x,y)


print ("Transitive closure matrix is: ")
g.transitiveClosure()
