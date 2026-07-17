class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0
        found = False
        while not found and index1 < len(nums)-1:
            for i in range(index1+1, len(nums)):
                index2 = i
                if nums[index1] + nums[index2] == target:
                    found = True
                    break
            if not found:   
                index1 += 1
                
        return list([index1, index2])