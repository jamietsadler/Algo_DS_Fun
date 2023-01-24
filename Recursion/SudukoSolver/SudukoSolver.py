from typing import List
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j])
                rows[i].add(val)
                cols[j].add(val)
                boxes[(i // 3)*3+j//3].add(val)
        
        def is_valid(r, c, val):
            box = (r//3 )*3 + c//3
            if val in rows[r] or val in cols[c] or val in boxes[box]:
                return False
            return True
        
        def backtrack(r, c):
            if r == n - 1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1

            # current grid has been filled
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            box_id = (r // 3) * 3 + c // 3
            for v in range(1, n + 1):
                if not is_valid(r, c, v):
                    continue

                board[r][c] = str(v)
                rows[r].add(v)
                cols[c].add(v)
                boxes[box_id].add(v)

                if backtrack(r, c + 1):
                    return True

                # backtrack
                board[r][c] = '.'
                rows[r].remove(v)
                cols[c].remove(v)
                boxes[box_id].remove(v)

            return False


        backtrack(0, 0)