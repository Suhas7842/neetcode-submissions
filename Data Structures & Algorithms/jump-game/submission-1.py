class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0
        l = len(nums)
        for i in range(len(nums)):
            if i > maxreach:
                return False
            if i+nums[i] > maxreach:
                maxreach = i+nums[i]
            if maxreach >= l-1:
                return True
        return False