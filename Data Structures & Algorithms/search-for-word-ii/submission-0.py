class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
    def addWord(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            root.addWord(w)
        ROWS,COLS=len(board),len(board[0])
        res,visit=set(),set()
        def dfs(r,c,cur,word):
            if r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visit or board[r][c] not in cur.children:
                return
            visit.add((r,c))
            cur=cur.children[board[r][c]]
            word+=board[r][c]
            if cur.isWord:
                res.add(word)
            dfs(r+1,c,cur,word)
            dfs(r-1,c,cur,word)
            dfs(r,c+1,cur,word)
            dfs(r,c-1,cur,word)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        return list(res)