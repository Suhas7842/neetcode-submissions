class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Map each character to its alien alphabet position
        rank = {}
        for i, char in enumerate(order):
            rank[char] = i
        # Compare adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            # Compare characters
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if rank[word1[j]] > rank[word2[j]]:
                        return False
                    # Correct order; no need to compare
                    # the remaining characters
                    break
            # Prefix case: "apple" before "app" is invalid
            else:
                if len(word1) > len(word2):
                    return False
        return True