class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        provinces=0
        visited=set()
        def dfs(city):
            visited.add(city)
            for nei in range(n):
                if isConnected[city][nei]==1 and nei not in visited:
                    dfs(nei)
        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces+=1
        return provinces

        