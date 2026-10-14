class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        sorted_hm = sorted(hm.items(), key=lambda item: item[1], reverse=True)
        k_more_frequent = [item[0] for item in sorted_hm[:k]]
        return k_more_frequent