class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_stack(self):
        return len(self.stack)

stack = Stack()
stack.push(453)
stack.push('ABC')
stack.push(354)
print("Peek: ", stack.peek())
print("Size: ", stack.size_stack())
print("Pop: ", stack.pop())
print("Pop: ", stack.pop())
print("Size: ", stack.size_stack())
