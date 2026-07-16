from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    q=deque([(r,c)])
                    grid[r][c]="0"
                    while q:
                        x,y=q.popleft()
                        for dx,dr in directions:
                            nx=x+dx
                            ny=y+dr
                            if  0<=nx<rows and 0<=ny<cols and grid[nx][ny]=="1" :
                                grid[nx][ny]="0"
                                q.append((nx,ny))
        return islands

        