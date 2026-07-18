from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()

        for r in range(rows):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][cols - 1] == "O":
                q.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == "O":
                q.append((0, c))
            if board[rows - 1][c] == "O":
                q.append((rows - 1, c))

        while q:
            x, y = q.popleft()

            if board[x][y] == "O":
                board[x][y] = "S"
            

            

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O":
                    q.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"