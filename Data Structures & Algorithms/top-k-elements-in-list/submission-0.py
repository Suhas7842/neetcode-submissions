class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        sorted_freq = sorted(d.items(), key=lambda x:x[1],reverse=True)
        return [key for key,freq in sorted_freq[:k]]