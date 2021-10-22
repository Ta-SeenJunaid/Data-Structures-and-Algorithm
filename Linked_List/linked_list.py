class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self, data):
        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.size = self.size+1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node



linked_list = LinkedList()
linked_list.insert_start(5)
linked_list.insert_start(45)
linked_list.insert_start(85)
linked_list.insert_end(100)
print("Size: ", linked_list.size)
print("Traversing")
linked_list.traverse()