'''
Here the time complexity is O(n^2)
'''
def maxSumSubArray(arr):
    best = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i,len(arr)):
            total += arr[j]
            best = max(total,best)
    return best


arr = [-1,2,4,-3,5,2,-5,2]
print(maxSumSubArray(arr))