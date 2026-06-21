class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minDist = [float('inf')] * n
        cost = 0
        for i in range(n - 1):
            nxt = i + 1
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                minDist[j] = min(minDist[j], d)
                if minDist[j] < minDist[nxt]:
                    nxt = j
            cost += minDist[nxt]
            points[nxt], points[i + 1] = points[i + 1], points[nxt]
            minDist[nxt] = minDist[i + 1]
        return cost