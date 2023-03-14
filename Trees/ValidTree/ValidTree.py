from typing import List
from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_dict = defaultdict(list)

        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbour in adj_dict[node]:
                
                dfs(neighbour)
                
        dfs(0)
        return n == len(seen)