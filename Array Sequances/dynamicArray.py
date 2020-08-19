import sys

n=10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data) #actual memory in bytes
    print ('Length: {0:3d}; Size in bytes: {1:4d} '.format(a,b))
    data.append(n) #increase length by one


#1: Alloc new array B with larger capacity (usually twice the existing size)
#2: set B[i] = A[i] for i=0...n-1, where n is curr number of items
#3: Set A=B
#4: Insert new elem in the new array

import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self,k):
        if not 0<= k < self.n:
            return IndexError('K is out of bounds')
        return self.A[k]

    def append(self, e):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = e
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print(len(arr))
arr.append(2)
print(len(arr))
print(arr[0])
print(arr[1])