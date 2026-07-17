class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        setterNS = list(set(nums))
        numsSort = sorted(setterNS)
        if len(numsSort) == 1:
            return 1
        count = [1] * len(numsSort)
        print(numsSort)
        i = 0
        for j in range(len(numsSort)-1):
            if numsSort[j] == numsSort[j+1]-1 or numsSort[j] == numsSort[j+1]+1:
                count[i] += 1
                print("j = ", numsSort[j], " j+1 = ", numsSort[j+1], "OK")
            else:
                print("j = ", numsSort[j], " j+1 = ", numsSort[j+1], "PAS OK")
                i += 1
            ans = int(max(count))
            print("ans = ", ans)
        return ans