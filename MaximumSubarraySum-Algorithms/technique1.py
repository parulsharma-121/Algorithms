'''
Here the given array is arr = [-1,2,4,-3,5,2,-5,2] and we have to find the maximum sum of subarray that is 10.
'''
def maxSumSubArray(arr):
    best = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            total = 0
            for k in range(i,j):
                total += arr[k]
            best = max(best,total)
    return best

arr = [-1,2,4,-3,5,2,-5,2]
print(maxSumSubArray(arr))