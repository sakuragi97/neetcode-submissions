class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        return sorted(counter, key=lambda num:counter[num], reverse=True)[:k]
        