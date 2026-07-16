from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        original=image[sr][sc]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque([(sr,sc)])
        rows=len(image)
        cols=len(image[0])
        image[sr][sc]=color
        while q:
            x,y=q.popleft()
            for dx,dy in directions:
                nx=x+dx
                ny=y+dy
                if 0<=nx<rows and 0<=ny<cols and image[nx][ny]==original:
                    image[nx][ny]=color
                    q.append((nx,ny))
        return image
        