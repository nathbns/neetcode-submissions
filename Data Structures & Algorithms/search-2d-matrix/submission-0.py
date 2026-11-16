class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for r in matrix:
            min_r, max_r = r[0], r[-1]
            if target < min_r:
                return False
            elif target > max_r:
                continue
            
            while r:
                mid = (len(r) // 2)
                if r[mid] > target:
                    r = r[:mid]
                elif r[mid] < target:
                    r = r[mid+1:]
                else:
                    return True
            
        return False