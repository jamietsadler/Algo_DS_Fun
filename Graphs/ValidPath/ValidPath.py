import collections
from typing import List

# DFS
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = [False]*n
        def dfs(curr_node):
            if curr_node == destination:
                return True
            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            
            return False
        
        return dfs(source)

# BFS 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = [False] * n
        seen[source] = True
        
        queue = collections.deque([source])
        
        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    queue.append(next_node)
                    seen[next_node] = True
        return False