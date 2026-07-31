class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap=defaultdict(int)
        for num in nums:
            countMap[num]+=1
        for key,val in countMap.items():
            if val>len(nums)//2:
                return key