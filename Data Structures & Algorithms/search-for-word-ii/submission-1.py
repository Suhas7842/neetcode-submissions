class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        ROWS, COLS = len(board), len(board[0])
        res = []
        def dfs(r, c, parent, ch):
            node = parent.children[ch]
            if node.word:
                res.append(node.word)
                node.word = None
            board[r][c] = "#"
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in node.children):
                    dfs(nr, nc, node, board[nr][nc])
            board[r][c] = ch
            if not node.children and node.word is None:
                del parent.children[ch]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root, board[r][c])
        return res