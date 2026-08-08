class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        l,r=0,n-k
        while l<r:
            mid=(l+r)//2
            if(x-arr[mid]<=arr[mid+k]-x):
                r=mid
            elif (x-arr[mid]>arr[mid+k]-x):
                l=mid+1
        return arr[l:l+k]