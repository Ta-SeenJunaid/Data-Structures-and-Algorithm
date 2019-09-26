from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*(len(self.graph))

        queue1 = []

        queue1.append(s)
        visited[s] = True

        while queue1:

            s = queue1.pop(0)
            print(s, end = " ")


            for i in self.graph[s]:
                if visited[i]== False:
                    queue1.append(i)
                    visited[i] = True



g = Graph()
edges = int(input("Enter the num of edges: "))

for z in range(0,edges):
    print("Input edge" , z+1)
    x=int(input("Enter edge starting node: "))
    y=int(input("Enter edge ending node: "))
    g.addEdge(x,y)

start = int(input("Enter the starting node:"))

g.BFS(start)
