class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        for c, count in s_count.items():
            if count != t_count[c]:
                return False
        
        for c, count in t_count.items():
            if count != s_count[c]:
                return False

        return True