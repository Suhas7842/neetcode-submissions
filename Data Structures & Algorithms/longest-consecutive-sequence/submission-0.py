class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set=set(nums)
        maxLen=0
        for num in nums_set:
            if num-1 not in nums_set:
                curr=num
                currLen=1
                while curr+1 in nums_set:
                    curr+=1
                    currLen+=1
                maxLen=max(currLen,maxLen)
        return maxLen