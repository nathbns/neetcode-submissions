class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        sorted_hmp = dict(
            sorted(
                hashmap.items(), 
                key=lambda x: x[1], 
                reverse=True
            )
        )
        ans = []
        count = 0
        for num in sorted_hmp.keys():
            if count != k:
                ans.append(num)
                count += 1
        return ans