class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}
        # Build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                graph[first_email].append(email)
                graph[email].append(first_email)
        visited = set()
        result = []
        def dfs(email, component):
            if email in visited:
                return
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, component)
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                component.sort()
                result.append([
                    email_to_name[email]
                ] + component)
        return result