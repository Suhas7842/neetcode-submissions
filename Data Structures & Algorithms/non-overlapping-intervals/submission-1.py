class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res=1
        prevEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end
                res+=1
        return len(intervals)-res