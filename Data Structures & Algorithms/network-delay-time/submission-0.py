class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,w in times:
            edges[u].append((v,w))
        visit=set()
        count=0
        minHeap=[(0,k)]
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            count=max(count,w1)
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return count if len(visit)==n else -1