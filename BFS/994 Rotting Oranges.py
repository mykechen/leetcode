# Multi-source BFS: all rotten oranges spread simultaneously, track minutes until no fresh remain
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        q = deque()
        minutes = 0
        fresh_cnt = 0
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # seed queue with all initially rotten oranges, count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:  # rotten orange
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        # process level by level — each level = 1 minute
        while q and fresh_cnt > 0:
            minutes += 1

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nr == m or nc < 0 or nc == n:
                        continue
                    if grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue

                    fresh_cnt -= 1  # rot this fresh orange
                    q.append((nr, nc))
                    grid[nr][nc] = 2

        return minutes if fresh_cnt == 0 else -1  # -1 if unreachable fresh oranges