import math

class Heap:
    def __init__(self, comparator = lambda x,y: x > y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)

    def delete(self):
        if self.get_size() == 0:
            return

        tail = self.storage.pop()
        if self.get_size() == 0:
            return tail

        head = self.storage[0]
        self.storage[0] = tail
        self._sift_down(0)
        return head

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index >= self.get_size():
            return

        parent_index = math.floor((index-1)/2)
        if parent_index < 0:
            return
        
        if self.comparator(self.storage[index], self.storage[parent_index]):
            temp = self.storage[parent_index]
            self.storage[parent_index] = self.storage[index]
            self.storage[index] = temp
            self._bubble_up(parent_index)

    def _sift_down(self, index):
        left_child_index = 2*index + 1
        right_child_index = 2*index + 2

        if left_child_index >= self.get_size():
            return
        
        swap_index = left_child_index

        if right_child_index < self.get_size() and self.comparator(self.storage[right_child_index], self.storage[left_child_index]):
            swap_index = right_child_index

        if self.comparator(self.storage[swap_index], self.storage[index]):
            temp = self.storage[index]
            self.storage[index] = self.storage[swap_index]
            self.storage[swap_index] = temp
            self._sift_down(swap_index)
