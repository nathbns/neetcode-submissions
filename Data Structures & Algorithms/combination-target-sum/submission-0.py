class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, res = [], []
        nums.sort()

        def backtracking(res: List[List[int]], idx: int, cnt: int) -> None:
            if cnt == target:
                ans.append(res[:])
            
            for i in range(idx, len(nums)):
                if nums[i] > target - cnt:
                    break
                res.append(nums[i])
                backtracking(res, i, cnt + nums[i])
                res.pop()
         
        backtracking(res, 0, 0)
        return ans