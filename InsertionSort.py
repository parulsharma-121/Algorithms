'''
Insertion Sort

'''
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr = [10,12,1,3,4,78,12,34]
print(insertionSort(arr))