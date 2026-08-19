class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            total,count=0,1
            mid=(l+r)//2
            for weight in weights:
                if total + weight > mid:
                    count += 1
                    total = 0
                total += weight
            if count<=days:
                r=mid-1
            else:
                l=mid+1
        return l