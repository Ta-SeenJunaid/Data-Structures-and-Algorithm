class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_node(self, data):
        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node


linked_list = LinkedList()
linked_list.insert_node(5)
linked_list.insert_node(45)
linked_list.insert_node(85)
print(linked_list.size)