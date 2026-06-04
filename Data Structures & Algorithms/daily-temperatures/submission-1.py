class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev_day=stack.pop()
                res[prev_day]=i-prev_day
            stack.append(i)
        return res