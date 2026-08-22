class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate[num] = False
        return False
