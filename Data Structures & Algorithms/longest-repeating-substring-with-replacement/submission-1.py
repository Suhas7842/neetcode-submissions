class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        count={}
        maxf=0
        left=0
        for right in range(len(s)):
            count[s[right]]=count.get(s[right], 0)+1
            maxf=max(count.values())
            window=right-left+1
            if window-maxf>k:
                count[s[left]]-=1
                left+=1
            res=max(res, right-left+1)
        return res