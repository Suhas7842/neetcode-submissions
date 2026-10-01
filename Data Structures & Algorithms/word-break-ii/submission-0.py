class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = {}
        def backtrack(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word not in words:
                    continue
                for suffix in backtrack(end):
                    if suffix:
                        res.append(word + " " + suffix)
                    else:
                        res.append(word)
            memo[start] = res
            return res
        return backtrack(0)