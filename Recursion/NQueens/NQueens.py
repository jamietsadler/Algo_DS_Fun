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