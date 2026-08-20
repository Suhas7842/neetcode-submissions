class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        while l<=r:
            mid=(l+r)//2
            total,count=0,1
            for num in nums:
                if total + num > mid:
                    count += 1
                    total = 0
                total += num
            if count<=k:
                r=mid-1
            else:
                l=mid+1
        return l