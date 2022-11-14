from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        
        stack = [0]
        
        while stack:
            room = stack.pop()
            for n in rooms[room]:
                if not seen[n]:
                    seen[n] = True
                    stack.append(n)
        
        return all(seen)