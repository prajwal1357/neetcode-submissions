class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                num = board[r][c]

                row = ("row", r, num)
                col = ("col", c, num)
                box = ("box", r // 3, c // 3, num)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True