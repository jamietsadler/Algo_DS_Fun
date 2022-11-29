from typing import List
from collections import defaultdict

class Solution:
        
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        children = defaultdict(list)
        ans = [[] for _ in range(n)]
        
        for x, y in edges:
            children[x].append(y)
        
        def dfs(x, curr):
            for child in children[curr]:
                if x in ans[child]:
                    continue
                ans[child].append(x)
                dfs(x, child)
        
        for i in range(n):
            dfs(i, i)
            
        return ans
        
        