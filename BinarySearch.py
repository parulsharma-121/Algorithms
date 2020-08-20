'''
Binary Search Algorithm
'''
def binarySearch(arr,x):
    mid = (len(arr))/2
    l = 0
    r = len(arr)-1
    while(l <= r): 
        mid = (l+r) // 2
        if(arr[mid] < x): 
            l = mid + 1
        elif(arr[mid] > x): 
            r = mid - 1
        else: 
            return mid 
    return -1
arr= [2,3,4,5,6,9,14]
x = 5
result = binarySearch(arr, x) 
  
if(result != -1): 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 