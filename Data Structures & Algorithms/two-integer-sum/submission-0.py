class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in lookup:
                return [lookup[diff],i]
            lookup[nums[i]]=i
        return []