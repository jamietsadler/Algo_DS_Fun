from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        def bfs(r, c):
            visited = set()
            queue = deque([])
            queue.append((r+1, c, 1))
            queue.append((r-1, c, 1))
            queue.append((r, c+1, 1))
            queue.append((r, c-1, 1))
            
            while queue:
                x, y, val = queue.popleft()
                if x < 0 or x >= ROWS or y < 0 or y >= COLS or (x, y) in visited or rooms[x][y] in [0, -1]:
                    continue
                visited.add((x, y))
                rooms[x][y] = min(rooms[x][y], val)
                queue.append((x+1, y, val+1))
                queue.append((x-1, y, val+1))
                queue.append((x, y+1, val+1))
                queue.append((x, y-1, val+1))
                
            
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    bfs(i, j)