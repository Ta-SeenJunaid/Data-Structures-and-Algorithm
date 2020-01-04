
class Heap(object):
    HEAP_LENGTH = 10

    def __init__(self):
        self.heap = [0]*Heap.HEAP_LENGTH
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


    def heapSort(self):

        for i in range(0, self.currentPosition+1):
            temp = self.heap[0]
            print(temp)
            self.heap[0]= self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i] = temp
            self.fixDown(0, self.currentPosition-i-1)


    def fixDown(self, index, upto):

        while index <= upto:

            leftChild = 2*index+1
            rightChild = 2*index+2

            if leftChild < upto:
                childToSwap = None

                if rightChild > upto:
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        childToSwap = leftChild
                    else:
                        childToSwap = rightChild

                if self.heap[index] < self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break

                index = childToSwap
            else:
                break
