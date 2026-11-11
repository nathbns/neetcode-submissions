class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        n = len(word)
        rows, cols = len(board), len(board[0])

        def backtracking(r: int, c: int, idx: int) -> bool:
            if board[r][c] == word[idx]:
                if idx == n - 1:
                    return True
                tmp = board[r][c]
                board[r][c] = "#"
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if backtracking(nr, nc, idx+1):
                        return True
                board[r][c] = tmp
            return False
        
        for i in range(rows):
            for j in range(cols):
                if backtracking(i, j, 0):
                    return True
        return False