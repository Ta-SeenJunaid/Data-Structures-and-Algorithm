
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


class DepthFirstSearch:
    def dfs(self, start_node):
        start_node.visited = True
        print(start_node.name)

        for n in start_node.adjacency_list:
            if not n.visited:
                self.dfs(n)


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

depth_first_search = DepthFirstSearch()
depth_first_search.dfs(a)
