class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen=float("inf")
        l=0
        windowSum=0
        for r in range(len(nums)):
            windowSum+=nums[r]
            while windowSum>= target:
                minLen=min(r-l+1,minLen)
                windowSum-=nums[l]
                l+=1
        return 0 if minLen == float("inf") else minLen