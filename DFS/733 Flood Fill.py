# DFS: starting from (sr, sc), fill all connected cells of same color with new color
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        neighbors = [[-1,0], [1,0], [0,1], [0,-1]]
        old = image[sr][sc]  # original color to replace
        m = len(image)
        n = len(image[0])

        def dfs(i, j):
            image[i][j] = color  # paint current cell
            for x, y in neighbors:
                nr = x + i
                nc = y + j
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == old:
                    dfs(nr, nc)

        if old != color:  # skip if already the target color (avoids infinite loop)
            dfs(sr, sc)

        return image