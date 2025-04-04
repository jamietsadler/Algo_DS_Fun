class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diagonals, anti_diagonals):
            if row == n:
                return 1
            solutions = 0
            
            for col in range(n):
                diag = row - col
                anti_diag = row + col
                
                if (col in cols 
                      or diag in diagonals 
                      or anti_diag in anti_diagonals):
                    continue

                
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                
                solutions += backtrack(row+1, cols, diagonals, anti_diagonals)
                
                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)
                
            return solutions
        
        return backtrack(0, set(), set(), set())
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(row, cols, diaganols, antidiaganols, state):
            if row == n:
                final = []
                for row in state:
                    tmp = "".join(row)
                    final.append(tmp)                   
                res.append(final[:])
                return 

            for col in range(n):
                diag = row - col
                anti_diag = col + row
                if col in cols or diag in diaganols or anti_diag in antidiaganols:
                    continue
                
                state[row][col] = 'Q'
                cols.add(col)
                diaganols.add(diag)
                antidiaganols.add(anti_diag)
                backtrack(row + 1, cols, diaganols, antidiaganols, state)

                state[row][col] = '.'
                cols.remove(col)
                diaganols.remove(diag)
                antidiaganols.remove(anti_diag)
        res = []
                
        board = [['.'] * n for _ in range(n)]
        backtrack(0, set(), set(), set(),board)
        return res

        