class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                idx = board[r][c]
                box_idx = (r//3)*3+(c//3)
                if idx==".":
                    continue
                if idx in rows[r] or idx in cols[c] or idx in boxes[box_idx]:
                    return False
                rows[r].add(idx)
                cols[c].add(idx)
                boxes[box_idx].add(idx)
        return True