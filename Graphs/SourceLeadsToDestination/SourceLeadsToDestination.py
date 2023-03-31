from typing import List
from collections import defaultdict
from functools import cache 

# Using list to mark nodes as visited in this path (cycle detection)
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        visited = [0] * n
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            
            if len(graph[node]) == 0:
                return node == destination
            visited[node] = -1
            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            visited[node] = 1
            return True
        
        return dfs(source)

# 0 for not visited;
# -1 for visited in current ongoing path, or "visiting";
# 1 for memo: all paths starting from the node are search and could reach destination, or "visited";


# Using cache for memosation and set to mark nodes currently visited on that path to detect cycles.
class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        visited = set()

        @cache
        def dfs(node):
            if node in visited:
                return False
            elif len(graph[node]) == 0:
                return node == destination
            
            visited.add(node)
            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            visited.remove(node)
            return True
        
        return dfs(source)

# Using colours to mark whether node has been visited
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
