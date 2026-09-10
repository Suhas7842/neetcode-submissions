class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
        reachable = [set() for _ in range(numCourses)]
        def dfs(course, start):
            for neighbor in graph[course]:
                if neighbor not in reachable[start]:
                    reachable[start].add(neighbor)
                    dfs(neighbor, start)
        for course in range(numCourses):
            dfs(course, course)
        return [v in reachable[u] for u, v in queries]