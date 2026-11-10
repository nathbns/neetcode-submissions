class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols, best = len(grid), len(grid[0]), 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            cnt = 1
            for dr, dc in directions:
                cnt += dfs(r + dr, c + dc)
            return cnt
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    best = max(best, dfs(i, j))
        return best


