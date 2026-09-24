class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        # (enqueueTime, processingTime, index)
        tasks = sorted(
            (enqueue, process, i)
            for i, (enqueue, process) in enumerate(tasks)
        )
        heap = []
        result = []
        time = 0
        i = 0
        while i < n or heap:
            # If no task is available, jump to the next enqueue time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]
            # Add every task that has become available
            while i < n and tasks[i][0] <= time:
                enqueue, process, index = tasks[i]
                heapq.heappush(heap, (process, index))
                i += 1
            # Process the task with smallest processing time
            process, index = heapq.heappop(heap)
            result.append(index)
            time += process
        return result