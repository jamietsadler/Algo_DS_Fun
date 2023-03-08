from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        position = 0
        speed = 1

        queue = deque([(position, speed, 0)])

        while queue:
            position, speed, moves = queue.popleft()

            if target == position:
                return moves
            
            queue.append((position + speed, speed * 2, moves +1))
            if speed > 0:
                if position + speed > target:
                    queue.append((position, -1, moves + 1))
            else:
                if position + speed < target:
                    queue.append((position ,  1, moves + 1))