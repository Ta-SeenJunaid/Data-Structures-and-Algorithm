
class Heap(object):
    HEAP_LENGTH = 10

    def __init__(self):
        self.heap = [0]*self.HEAP_LENGTH
        self.currentPosition = -1


    def insert(self, data):
        if self.heapFull():
            print("Heap is full!!!!!!!!!!!!!!!!!")
            return

        self.currentPosition = self.currentPosition + 1
        self.heap[self.currentPosition] = data
        self.fixUp(self.currentPosition)


    def fixUp(self, index):
        parentIndex = int((index - 1) / 2)

        while (parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]):
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            parentIndex = int((index - 1) / 2)




    def heapFull(self):
        if self.currentPosition == self.HEAP_LENGTH:
            return True
        else:
            return False
