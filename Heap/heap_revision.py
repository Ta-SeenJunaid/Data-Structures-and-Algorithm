
class Heap:

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * self.HEAP_SIZE
        self.current_position = -1

    def insert(self, item):
        if self.is_full():
            print("The heap is full")
            return
        else:
            self.current_position = self.current_position + 1
            self.heap[self.current_position] = item
            self.fix_up(self.current_position)

    def is_full(self):
        if self.current_position == self.HEAP_SIZE:
            return True
        else:
            return False

    def heap_sort(self):
        for i in range(0, self.current_position):
            temp = self.heap[0]
            print(temp)
            self.heap[0] = self.heap[self.current_position - i]
            self.heap[self.current_position - i] = temp
            self.fix_down(0, self.current_position -i -1)

    def fix_up(self, index):
        parent_index = int((index-1)/2)

        while parent_index >= 0 and self.heap[parent_index] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp
            parent_index = int((parent_index-1)/2)

    def fix_down(self, start, end):
        pass
