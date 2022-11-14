# DFS
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        clone_node = Node(node.val, [])
        
        self.visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return self.visited[node]



# BFS 
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        if not node:
            return None
        
        queue = deque([node])
        
        visited[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            
            for nbr in n.neighbors:
                if nbr not in visited:
                    visited[nbr] = Node(nbr.val, [])
                    queue.append(nbr)
                visited[n].neighbors.append(visited[nbr])
        
        return visited[node]