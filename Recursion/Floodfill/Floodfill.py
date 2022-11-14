
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        R, C = len(image), len(image[0])
        if image[sr][sc] == color:
            return image
        old_color = image[sr][sc]
        
        def dfs(r, c):
            if image[r][c] == old_color:
                image[r][c] = color
            
                if r >= 1: 
                    dfs(r-1, c)
                if r +1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c + 1< C:
                    dfs(r, c+1)
        
        dfs(sr, sc)
        return image