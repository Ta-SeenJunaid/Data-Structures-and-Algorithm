class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size_stack(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(453)
queue.enqueue('ABC')
queue.enqueue(354)
print("Current Queue: ", queue.queue)
print("Peek: ", queue.peek())
print("Size: ", queue.size_stack())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Size: ", queue.size_stack())
