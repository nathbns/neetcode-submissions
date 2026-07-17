class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        select = 0
        ans = []
        for selected in range(len(nums)):
            select = selected
            prod = 1
            for i, num in enumerate(nums):
                if select != i:
                    prod *= num
            ans.append(prod)
        return ans