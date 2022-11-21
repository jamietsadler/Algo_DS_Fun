class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if 1<= n <= 2:
            return 1
        x, y, z = 0,1, 1
        for i in range(2,n):
            x, y, z = y, z, x + y + z
        return z

class Solution:
    def __init__(self):
        self.memo = {}
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self.memo[n]