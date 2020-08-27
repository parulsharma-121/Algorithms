'''Selection Sort'''
def selectionSort(arr):
    for i in range(len(arr)-1):
        minIndex = i
        for j in range(i+1,len(arr)-1):
            if(arr[j]<arr[minIndex]):
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr 
arr = [2,1,4,66,45,23,90]
print(selectionSort(arr))