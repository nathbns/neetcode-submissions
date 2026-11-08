class Solution:



    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # up, down, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        
        def dfs(r: str, c: str) -> None:
            # out of grid
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0"):
                return
            
            # else mark as seen
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(dr + r, dc + c)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands