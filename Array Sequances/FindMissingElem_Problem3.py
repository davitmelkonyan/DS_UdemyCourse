# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.

#sort both

def finder(arr1, arr2): #(O(NlogN))
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr[-1]

import collections

def finder2(arr1,arr2):
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] +=1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num]-=1

def finder3(arr1,arr2):
    r = 0
    for num in arr1+arr2: #concetination
        r ^= num #xor
        #print (r)
    return r



arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print (finder3(arr1,arr2))

