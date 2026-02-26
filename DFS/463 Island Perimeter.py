# Count perimeter by giving each land cell 4 sides, subtracting 2 for each shared edge
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # SOL1: DFS — each out-of-bounds or water neighbor adds 1 to perimeter
        # perimeter = 0
        # m = len(grid)
        # n = len(grid[0])
        # neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # visited = set()

        # def dfs(i, j):
        #     if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
        #         return 1
        #     if (i, j) in visited:
        #         return 0

        #     visited.add((i, j))

        #     return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] == 1:
        #             return dfs(r, c)

        # SOL2: counting — each land cell starts with 4 edges, subtract shared edges
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    perimeter += 4  # start with 4 sides
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2  # shared edge with top neighbor
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2  # shared edge with left neighbor

        return perimeter