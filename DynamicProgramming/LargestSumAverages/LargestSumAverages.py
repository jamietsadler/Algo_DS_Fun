from functools import lru_cache
from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        cusum = [0]
        for x in nums: 
            cusum.append(cusum[-1] + x) # get cumulative sum of array
        print(cusum)
        n = len(nums)

        @lru_cache(None)
        def dp(i, k):
            if i>=n:
                return 0
            if k == 1:
                return (cusum[-1]-cusum[i])/(n-i) # calculate remaining average
            return max((cusum[j+1]-cusum[i])/(j-i+1) + dp(j+1, k-1) for j in range(i, n-k+1))
        
        return dp(0, k)

# Each state, we are get the maximum from about n values, so the complexity for each state of O(n).
# The final time complexity will be O(kn^2)

class Solution:
    def largestSumOfAverages(self, A, K):
    
        dp=[[0 for j in range(K)] for i in A]
        
        
        for j in range(len(A)):
            for i in range(K): 
                if i==0:
                    dp[j][i]=sum(A[:j+1])/float(len(A[:j+1]))
                else:
                    if len(A[:j+1])<i+1:
                        break
                    for k in range(j):
                        
                        dp[j][i]=max(dp[k][i-1]+sum(A[k+1:j+1])/float(len(A[k+1:j+1])),dp[j][i])
                        

        return dp[-1][-1]