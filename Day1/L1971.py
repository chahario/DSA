from collections import deque
class Solution:
    # birectional graph.
    def validPathBFS(self, n, edges, source, destination):
        if source == destination:
            return 
        graph = [[] for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q = deque([source])
        visited = [False] * n
        visited[source] = True

        while q:
            node = q.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)

        return False
        

        

# n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5