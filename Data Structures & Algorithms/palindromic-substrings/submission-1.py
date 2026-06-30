class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n=len(s)
        if n <= 1:
            return n
        if len(set(s)) == 1:
            return n * (n + 1) // 2
        for i in range(n):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res