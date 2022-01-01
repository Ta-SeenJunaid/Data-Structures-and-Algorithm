
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


class BreadthFirstSearch:
    def bfs(self, start_node):
        queue = [start_node]
        start_node.visited = True

        while queue:
            actual_node = queue.pop(0)
            print(actual_node.name)
            for n in actual_node.adjacency_list:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.adjacency_list.append(b)
a.adjacency_list.append(f)
a.adjacency_list.append(g)
b.adjacency_list.append(c)
b.adjacency_list.append(d)
d.adjacency_list.append(e)
g.adjacency_list.append(h)
f.adjacency_list.append(d)

breadth_first_search = BreadthFirstSearch()
breadth_first_search.bfs(a)