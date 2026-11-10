class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if total % 2 != 0:
            return False
        
        memo = {}
        def dfs(index: int, acc: int) -> bool:
            if acc == target:
                return True
            elif index >= len(nums):
                return False

            n = nums[index]
            memo[(index, acc)] = dfs(index+1, acc+n) or dfs(index+1, acc)
            return memo[(index, acc)]
        
        return dfs(0, 0)
