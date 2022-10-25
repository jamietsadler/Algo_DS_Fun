# Bottom up iterative
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        prev = 0
        nex = 1
        
        for i in range(2, n+1):
            total = nex + prev
            prev = nex
            nex = total
        
        return nex


# Top down recursion and memoization
class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, n: int) -> int:
        
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n - 1) + self.fib(n-2)
        return self.cache[n]
        