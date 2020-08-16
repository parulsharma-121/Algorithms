'''
Given an array arr[] of n elements, write a function to search a given element x in arr[].

example: 
input : arr = [23,45,30,43,11,21,90]
        x = 30
output : 2 because 30 is present at 2nd index of array arr

input : arr = [23,45,30,43,11,21,90]
        x = 100
output : -1 because 100 is not present in the array.
'''

def linearSearch(x,arr):
    for i in range(len(arr)):
        if(arr[i]==x):
            return i
    return -1

x = 11
arr = [23,45,30,43,11,21,90]
print(linearSearch(x,arr))