# DFS from border: mark border-connected "O"s as safe, then capture the rest
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != "O":
                return

            board[r][c] = "#"  # mark as safe (connected to border)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # step 1: DFS from all border "O"s to mark them as safe
        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                    dfs(r, c)

        # step 2: capture surrounded "O"s, restore safe "#"s back to "O"
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"  # surrounded — capture
                elif board[r][c] == "#":
                    board[r][c] = "O"  # border-connected — restore