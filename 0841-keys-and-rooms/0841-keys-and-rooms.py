from collections import defaultdict,deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph=defaultdict(list)
        visited={0}
        n=len(rooms)
        for i in range(n):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])
        q=deque([0])
        while q:
            node=q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        if len(visited)==n:
            return True
        else:
            return False
        
        