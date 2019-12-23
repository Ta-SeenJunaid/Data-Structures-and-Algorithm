class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjancencyList = []
        self.visited = False



class BreadthFirstSearch(object):

    def bfs(self, startNode):

        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:

            node = queue.pop(0)
            print(node.name)

            for n in node.adjancencyList:
                if not n.visited:
                    queue.append(n)
                    n.visited = True



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")

node1.adjancencyList.append(node2)
node1.adjancencyList.append(node3)

node2.adjancencyList.append(node4)
node2.adjancencyList.append(node5)

node3.adjancencyList.append(node6)

result = BreadthFirstSearch()
result.bfs(node1)
