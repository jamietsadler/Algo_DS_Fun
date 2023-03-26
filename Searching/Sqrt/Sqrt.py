class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x
        
        left = 2
        right = x // 2

        while left <= right:
            pivot = (left+right)//2
            ans = pivot*pivot
            if ans > x:
                right = pivot - 1
            elif ans < x:
                left = pivot + 1
            else:
                return pivot
        
        return right