class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_count = max(counts)
        occurrences = counts.count(max_count)
        # max_count - 1 is the number of gaps
        # n - occurrences + 1 is the gap size
        # max_count * occurrences is the max frequency tasks
        return max(
            len(tasks), 
            (max_count - 1) * (n - occurrences + 1) + max_count * occurrences
        )