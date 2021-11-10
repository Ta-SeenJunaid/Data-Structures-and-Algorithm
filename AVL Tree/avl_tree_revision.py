
class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left_child = None
        self.right_child = None


class AVL:

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):

        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        return self.settle_violation(data, node)

    def settle_violation(self, data, node):

        balance = self.calc_balance(node)

        if balance > 1 and data < node.left_child.data:
            print("Left left heavy situation")
            return self.rotate_right(node)
        if balance < -1 and data > node.right_child.data:
            print("Right right heavy situation")
            return self.rotate_left(node)
        if balance > 1 and data > node.left_child.data:
            print("Left right heavy situation")
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and data < node.right_child.data:
            print("Right left heavy situation")
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def in_order_traverse(self):
        if self.root:
            self.in_order_traverse_helper(self.root)

    def in_order_traverse_helper(self, node):
        if node.left_child:
            self.in_order_traverse_helper(node.left_child)

        print(node.data)

        if node.right_child:
            self.in_order_traverse_helper(node.right_child)

    def calc_height(self, node):
        if not node:
            return -1

        return node.height

    def calc_balance(self, node):

        if not node:
            return 0

        return self.calc_height(node.left_child) - self.calc_height(node.right_child)

    def rotate_right(self, node):

        new_parent_node = node.left_child
        new_parent_node_previous_right_child = new_parent_node.right_child

        new_parent_node.right_child = node
        node.left_child = new_parent_node_previous_right_child

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        new_parent_node.height = max(self.calc_height(new_parent_node.left_child),
                                     self.calc_height(new_parent_node.right_child)) + 1
        return new_parent_node

    def rotate_left(self, node):

        new_parent_node = node.right_child
        new_parent_node_previous_left_child = new_parent_node.left_child

        new_parent_node.left_child = node
        node.right_child = new_parent_node_previous_left_child

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        new_parent_node.height = max(self.calc_height(new_parent_node.left_child),
                                     self.calc_height(new_parent_node.right_child)) + 1

        return new_parent_node

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):

        # Not sure, might be unnecessary
        if not node:
            return node

        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print("Removing a leaf node.")
                del node
                return None
            if not node.left_child:
                print("Removing a node with only right child.")
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print("Removing a node with only left child")
                temp_node = node.left_child
                del node
                return temp_node

            print("Removing node with 2 children")
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)

        # If the tree had just a single node
        if not node:
            return node

        node.height = max(self.calc_height(node.left_child), self.calc_height(node.right_child)) + 1
        
        balance = self.calc_balance(node)


    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node


avl = AVL()

avl.insert(105)
avl.insert(103)
avl.insert(104)

avl.insert(30)
avl.insert(40)
avl.insert(50)


avl.insert(29)
avl.insert(28)
avl.insert(27)

avl.insert(15)
avl.insert(17)
avl.insert(16)

avl.insert(1000)
avl.insert(2000)

avl.in_order_traverse()




