# Multi-source BFS: start from all 0s and expand outward to find shortest distance for each cell
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        q = deque()
        visited = set()
        m, n = len(mat), len(mat[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # seed queue with all 0-cells as starting points
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        # BFS layer by layer — each layer increments distance by 1
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    mat[nr][nc] = mat[r][c] + 1 # distance = parent's distance + 1
                    q.append((nr, nc))
                    visited.add((nr, nc))

        return mat