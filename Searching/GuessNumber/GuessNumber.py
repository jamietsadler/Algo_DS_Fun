def guess():
    pass 

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            pick = (left+right)//2
            ans = guess(pick)
            if ans == -1:
                right = pick -1
            elif ans == 1:
                left = pick + 1
            else:
                return pick

        return -1