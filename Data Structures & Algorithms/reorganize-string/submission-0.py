class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        result = []
        prev_freq = 0
        prev_char = ""
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)
            # Put the previous character back now that
            # it is safe to use again.
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            freq += 1  # used one occurrence
            prev_freq = freq
            prev_char = char
        if len(result) != len(s):
            return ""
        return "".join(result)