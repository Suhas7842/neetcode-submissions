class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posDiag=set()
        negDiag=set()
        res=[]
        queens = [-1] * n
        def backtrack(r):
            if r==n:
                board = []
                for row in range(n):
                    line = ['.'] * n
                    line[queens[row]] = 'Q'
                    board.append("".join(line))
                res.append(board)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                queens[r] = c
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                queens[r] = -1
        backtrack(0)
        return res