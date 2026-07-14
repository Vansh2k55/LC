from collections import defaultdict,deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        visited={source}
        q=deque([source])
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return False
        