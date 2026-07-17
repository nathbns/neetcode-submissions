class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        ans = 0

        while i < len(heights) - 1:
            hi = heights[i]
            for j in range(i+1, len(heights)):
                hj = heights[j]
                h_current = min(hi, hj)
                longueur = j - i
                volume = h_current * longueur
                ans = max(volume, ans)
            i += 1
        
        return ans