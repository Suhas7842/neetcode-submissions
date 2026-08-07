class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        def isPalin(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return isPalin(l+1,r) or isPalin(l,r-1)
        return True