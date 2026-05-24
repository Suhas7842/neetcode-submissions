class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s): return ""
        count,window={},{}
        start,minLen=0,float('inf')
        for i in range(len(t)):
            count[t[i]] = 1+count.get(t[i],0)
        unique,required=len(count),0
        l=0
        for r in range(len(s)):
            window[s[r]] = 1+window.get(s[r],0)
            if s[r] in count and window[s[r]]==count[s[r]]:
                required+=1
            while required==unique:
                length=r-l+1
                if length<minLen:
                    minLen=length
                    start=l
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    required-=1
                l+=1
        return s[start:start+minLen] if minLen!=float('inf') else ""