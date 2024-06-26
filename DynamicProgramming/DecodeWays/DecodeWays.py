
class Solution(object):
    def numDecodings(self, s):
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):

            if 0 < int(s[i-1:i]) <= 9:
                dp[i] = dp[i-1]

            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]


class Solution(object):
    def __init__(self):
        self.memo = {}

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.recurse(0, s)

    def recurse(self, index, s):
        if index in self.memo:
            return self.memo[index]
        if index == len(s):
            return 1
        
        if s[index] == "0":
            return 0
        
        if index == len(s) - 1:
            return 1
        
        answer = self.recurse(index+1, s)
        if int(s[index:index+2]) <= 26:
            answer += self.recurse(index + 2, s)

        self.memo[index] = answer
        
        return answer