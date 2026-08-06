class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefixSum=[[0]*(cols+1) for _ in range(rows+1)]
        for i in range(1,rows+1):
            for j in range(1,cols+1):
                self.prefixSum[i][j]=self.prefixSum[i - 1][j] + self.prefixSum[i][j - 1] - self.prefixSum[i - 1][j - 1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSum[row2 + 1][col2 + 1]
            - self.prefixSum[row1][col2 + 1]
            - self.prefixSum[row2 + 1][col1]
            + self.prefixSum[row1][col1]
        )
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)