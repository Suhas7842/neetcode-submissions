class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}
        for course,prerequisite in prerequisites:
            preMap[course].append(prerequisite)
        visiting,visited=set(),set()
        res=[]
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for prerequisite in preMap[course]:
                if not dfs(prerequisite):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res