class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [] 
        for selected in range(len(nums)):
            prod = 1
            for i, num in enumerate(nums):
                if selected != i:
                    prod *= num
            ans.append(prod)
        return ans