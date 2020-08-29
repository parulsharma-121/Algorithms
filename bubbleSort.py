'''
Bubble Sort
'''
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr = [2,1,6,4,8,6,7,45,32,90,100,32]
print(bubbleSort(arr))