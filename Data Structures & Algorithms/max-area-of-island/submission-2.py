from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols, best = len(grid), len(grid[0]), 0

        def bfs(r: int, c: int) -> int:
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            area = 1

            while q:
                ro, co = q.popleft()
                for dr, dc in directions:
                    nr, nc = ro+dr, co+dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    area += 1
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    best = max(best, bfs(i, j))
        return best
            



