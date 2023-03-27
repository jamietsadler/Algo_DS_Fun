from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def neighbours(node):            
            output = []
            for i in range(len(node)):
                for d in [1, -1]:
                    x = (int(node[i]) + d) % 10 
                    num = node[:i] + str(x) + node[i+1:]
                    output.append(num)
            return output
        
        visited = set()
        queue = deque([('0000', 0)])
        while queue:
            node, dist = queue.popleft()
            if node == target:
                return dist
            if node in deadends:
                continue
            for nbr in neighbours(node):
                if nbr in visited:
                    continue
                queue.append((nbr, dist + 1))
                visited.add(nbr)

        return -1