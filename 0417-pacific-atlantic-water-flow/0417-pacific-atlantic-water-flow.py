from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pacific = set()
        atlantic = set()
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        for c in range(cols):
            pacific.add((0, c))
            atlantic.add((rows - 1, c))

        for r in range(rows):
            pacific.add((r, 0))
            atlantic.add((r, cols - 1))
        def bfs(start):
            visited=set(start)
            q=deque(start)
            while q:
                x,y=q.popleft()
                for dx,dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited and heights[nx][ny]>=heights[x][y]:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            return visited
        pacific=bfs(pacific)
        atlantic=bfs(atlantic)
        ans=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        return ans

