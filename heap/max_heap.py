from unittest.mock import MagicMock


class Heap:
    def __init__(self):
        self.storage = []

    # * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
    def insert(self, value):
        # place new value at end of tree
        self.storage.append(value)
        # check if larger then parent until in correct position
        i = len(self.storage)-1
        self._bubble_up(i)

    # * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed.

    def delete(self):

        # swap the first and last elements
        temp = self.storage[0]

        self.storage[0] = self.storage[len(self.storage)-1]

        self.storage[len(self.storage)-1] = temp

        # remove the last element
        rev = self.storage[len(self.storage)-1]
        del self.storage[len(self.storage)-1]
        # run a loop on the first element till its in the right spot
        i = 0
        print('after', self.storage)

        self._sift_down(i)
        return rev
       # * `get_max` returns the maximum value in the heap _in constant time_.

    def get_max(self):
        return self.storage[0]


# * `get_size` returns the number of elements stored in the heap.

    def get_size(self):
        return len(self.storage)


# * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.

    def _bubble_up(self, index):
        i = index
        # if i == 0:
        #     return
        while i >= 0:
            print('i', i, self.storage[i])

            if i < 3:
                parent = 0
            else:
                parent = (i-1)//2
            print(parent, self.storage[i], self.storage[parent])
            # check if parent is smaller, yes then  swap, no then return
            if self.storage[i] <= self.storage[parent]:
                return 0
            else:
                temp = self.storage[i]
                self.storage[i] = self.storage[parent]
                self.storage[parent] = temp
                i = parent

    # * `_sift_down` grabs the indices of this element's children and determines which child has a larger value.
    #     If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

    def _sift_down(self, index):
        left_i = (2*index) + 1
        right_i = (2*index) + 2

        left = True
        right = True
        if left_i > len(self.storage)-1:
            left = False
        if right_i > len(self.storage)-1:
            right = False

        if left or right:
            if not left:
                child = right_i
            elif not right:
                child = left_i
            else:
                if self.storage[left_i] > self.storage[right_i]:
                    child = left_i
                else:
                    child = right_i
        else:
            return True

        current = self.storage[index]
        if current <= self.storage[child]:
            temp = self.storage[index]
            self.storage[index] = self.storage[child]
            self.storage[child] = temp
            return self._sift_down(child)
        else:
            return True


heap = Heap()
# heap.insert(6)
# heap.insert(8)
# heap.insert(10)
# heap.insert(9)
# heap.insert(1)
# heap.insert(9)
# heap.insert(9)
# heap.insert(5)
# print(heap.storage, [10, 9, 9, 6, 1, 8, 9, 5])

# heap.insert(6)
# heap.insert(8)
# heap.insert(10)
# heap.insert(9)
# heap.insert(1)
# heap.insert(9)
# heap.insert(9)
# heap.insert(5)
# print(heap.get_size(), 8)
# print(heap.get_max(), 10)
# print(heap.storage)

# heap.insert(6)
# heap.insert(8)
# heap.insert(10)
# heap.insert(9)
# heap.insert(1)
# heap.insert(9)
# heap.insert(9)
# heap.insert(5)
# # print(heap.storage)
# heap.delete()
# # print(heap.storage)
# print(heap.get_max(), 9)
# heap.delete()
# # print(heap.storage)
# print(heap.get_max(), 9)
# heap.delete()
# # print(heap.storage)
# print(heap.get_max(), 9)
# heap.delete()
# print(heap.get_max(), 8)
# heap.delete()
# print(heap.get_max(), 6)
# heap._bubble_up = MagicMock()
# heap.insert(5)
# print(heap._bubble_up.called)
heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)
print(heap.storage)

descending_order = []

while heap.get_size() > 0:
    descending_order.append(heap.delete())

print(descending_order, [10, 8, 7, 6, 5, 5, 2, 1])
