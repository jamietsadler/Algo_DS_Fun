from typing import List
from functools import cache
from collections import deque

# Top Down DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return False
        
        @cache
        def helper(s, index):
            if index == len(s):
                return True
            
            for j in range(index+1, len(s)+1):
                if s[index:j] in wordDict and helper(s, j):
                    return True
            return False
        
        return helper(s, 0)

# BFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        queue = deque([0])
        visited = set()

        while queue:
            start = queue.popleft()
            if start in visited:
                continue

            for end in range(start, len(s) + 1):
                if s[start:end] in wordDict:
                    queue.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        
        return False
    
# Bottom up DP 
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
                
        return dp[len(s)]