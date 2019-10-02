from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfsUlit(self, v, visited):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsUlit(i, visited)


    def motherVertex(self):

        visited = [False]*(self.vertices)

        v = 0

        for i in range(self.vertices):
            if visited[i]==False:
                self.dfsUlit(i,visited)
                v = i

        visited = [False]*(self.vertices)
        self.dfsUlit(v, visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v


edges = int(input("Enter the num of edges: "))

g = Graph(edges-1)

for z in range(0, edges):
    print("Input edge" , z+1)
    x=int(input("Enter edge starting node: "))
    y=int(input("Enter edge ending node: "))
    g.addEdge(x,y)


print("A mother vertex is " + str(g.motherVertex()))
