class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        numPiles=len(piles)
        sumPiles=0
        for pile in piles:
            sumPiles+=pile
        left=((sumPiles-1)//h)+1
        right=((sumPiles-numPiles)//(h-numPiles+1)+1)
        while(left<right):
            mid = (left+right)//2
            totalTime=0
            for pile in piles:
                totalTime+=(pile-1)//mid+1
            if totalTime<=h:
                right=mid
            else:
                left=mid+1
        return left