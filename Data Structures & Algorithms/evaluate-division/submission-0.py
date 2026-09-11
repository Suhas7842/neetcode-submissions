class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        def dfs(current, target, product, visited):
            if current == target:
                return product
            visited.add(current)
            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    result = dfs(
                        neighbor,
                        target,
                        product * weight,
                        visited
                    )
                    if result != -1:
                        return result
            return -1
        answer = []
        for start, end in queries:
            if start not in graph or end not in graph:
                answer.append(-1.0)
            else:
                answer.append(
                    dfs(start, end, 1.0, set())
                )
        return answer