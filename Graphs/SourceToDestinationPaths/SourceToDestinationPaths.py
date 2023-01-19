from typing import List
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph or len(graph) == 0:
            return []
        paths = []
        
        queue = deque()
        path = [0]
        queue.append(path)
        
        while queue:
            curr_path = queue.popleft()
            curr_node = curr_path[-1]
            for next_node in graph[curr_node]:
                temp_path = curr_path.copy()
                temp_path.append(next_node)
                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        
        return paths