class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        result=0
        ans=set()
        for right in range(len(s)):
            while s[right] in ans:
                ans.remove(s[left])
                left+=1
            ans.add(s[right])
            result=max(result,right-left+1)
        return result