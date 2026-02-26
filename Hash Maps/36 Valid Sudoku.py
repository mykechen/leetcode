# Hash sets: track seen digits per row, column, and 3x3 box
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)  # row index -> set of digits
        cols = defaultdict(set)  # col index -> set of digits
        grid = defaultdict(set)  # (row//3, col//3) -> set of digits in 3x3 box

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # check if digit already exists in same row, col, or box
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in grid[(r//3,c//3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                grid[(r//3, c//3)].add(board[r][c])

        return True
