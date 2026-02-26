# DFS: count connected components — each unvisited "1" starts a new island
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        islands = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            grid[r][c] = "#"  # mark visited by modifying grid
            for dr, dc in neighbors:
                nr = dr + r
                nc = dc + c

                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)  # sink the entire island
                    islands += 1

        return islands