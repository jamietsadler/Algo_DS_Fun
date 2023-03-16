from typing import List
from collections import defaultdict

class Solution:
    WHITE = 1
    GREY  = 2
    BLACK = 3
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        state = [Solution.WHITE] * n

        def dfs(node):
            if state[node] != Solution.WHITE:                
                return state[node] == Solution.BLACK

            if len(graph[node]) == 0:
                return node == destination
            
            state[node] = Solution.GREY

            for chd in graph[node]:
                if not dfs(chd):
                    return False

            state[node] = Solution.BLACK
            return True

        return dfs(source)
