from typing import List
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
        
        seen = set()
        count = 0

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbour in adj_dict[node]:
                dfs(neighbour)

        for node in range(n):
            if node not in seen:
                count += 1
                dfs(node)

        return count
        