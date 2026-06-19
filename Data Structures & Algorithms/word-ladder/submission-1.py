class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbor=collections.defaultdict(list)
        wordList.append(beginWord)
        visit=set([beginWord])
        q=deque([beginWord])
        count=1
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                neighbor[pattern].append(word)
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return count
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neighborWord in neighbor[pattern]:
                        if neighborWord not in visit:
                            visit.add(neighborWord)
                            q.append(neighborWord)
                    neighbor[pattern]=[]
            count+=1
        return 0