class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9
        
        rows = [set() for i in range(N)]
        cols = [set() for i in range(N)]        
        boxes = [set() for i in range(N)]
        
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    continue
                
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                
                box_idx = i//3 * 3 + j//3
                if board[i][j] in boxes[box_idx]:
                    return False
                boxes[box_idx].add(board[i][j])
                
        return True

    