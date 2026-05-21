class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        l,r=0,len(heights)-1
        max_height=max(heights)
        while l<r:
            if heights[l]<heights[r]:
                curr_area=(r-l)*heights[l]
                l+=1
            else:
                curr_area=(r-l)*heights[r]
                r-=1
            max_area=max(max_area,curr_area)
            if max_height * (r-l) < max_area:
                break
        return max_area