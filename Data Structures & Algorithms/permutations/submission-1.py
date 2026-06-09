class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res,curr = [],[]
        seen = set()

        def backtrack(i):
            if i == n:
                res.append(curr[:])
                return
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)
                    backtrack(i+1)
                    seen.remove(num)
                    curr.pop()
        backtrack(0)
        return res