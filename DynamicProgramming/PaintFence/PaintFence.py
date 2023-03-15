from functools import lru_cache 

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        if n == 1:
            return k
        
        one_back = k**2
        two_back = k

        for i in range(3, n+1):
            tmp = (k-1) * (one_back + two_back)
            two_back = one_back
            one_back = tmp

        return one_back


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        @lru_cache
        def recurse(i):
            if i == 1:
                return k
            if i == 2:
                return k*k
            
            return (recurse(i-1) + recurse(i-2)) * (k-1)

        return recurse(n)