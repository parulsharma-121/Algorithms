'''
So this technique is most efficent with complexity of O(n).
'''
def maxSumSubArray(arr):
    best = 0
    total = 0
    for i in range(len(arr)):
        total = max(arr[i],total+arr[i])
        best = max(best,total)
    return best

arr = [-1,2,4,-3,5,2,-5,2]
print(maxSumSubArray(arr))