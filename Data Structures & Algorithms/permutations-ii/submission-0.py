class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        used = [False] * len(nums)
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicate choices at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrack()
                curr.pop()
                used[i] = False
        backtrack()
        return res