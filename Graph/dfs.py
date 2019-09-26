from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfsutil(self, v, visited):
        visited[v] = True
        print( v, end = ' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfsutil(i,visited)


    def DFS(self, s):
        visited = [False]*(len(self.graph))

        self.dfsutil(s,visited)




g = Graph()
edges = int(input("Enter the num of edges: "))

for z in range(0,edges):
    print("Input edge" , z+1)
    x=int(input("Enter edge starting node: "))
    y=int(input("Enter edge ending node: "))
    g.addEdge(x,y)

start = int(input("Enter the starting node:"))

g.DFS(start)
