from collections import defaultdict

class Graph:

    def __init__(self, V):

        self.graph = defaultdict(list)
        self.V = V

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalsortUtil(self, j, visited2, stack2):

        visited2[j] = True

        for k in self.graph[j]:
            if visited2[k] == False:
                self.topologicalsortUtil(k , visited2, stack2)

        stack2.insert(0, j)

    def topologicalSort(self):

        visited1 = [False]*self.V
        stack1 = []

        for i in range(self.V):
            if visited1[i] == False:
                self.topologicalsortUtil(i, visited1, stack1)

        print(stack1)

edges = int(input("Enter the num of edges: "))
vertices = int(input("Enter the num of vertices: "))

g = Graph(vertices)
for z in range(0,edges):
    print("Input edge" , z+1)
    x=int(input("Enter edge starting node: "))
    y=int(input("Enter edge ending node: "))
    g.addEdge(x,y)


print ("Topological sort is: ")
g.topologicalSort()

