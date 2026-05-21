class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        res=0
        maxLeft,maxRight=height[l],height[r]
        while(l<=r):
            if maxLeft<maxRight:
                maxLeft=max(maxLeft,height[l])
                res+=maxLeft-height[l]
                l+=1
            else:
                maxRight=max(maxRight,height[r])
                res+=maxRight-height[r]
                r-=1
        return res