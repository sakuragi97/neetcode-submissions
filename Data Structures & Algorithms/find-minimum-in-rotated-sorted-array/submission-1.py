class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:      
            return nums[left]
        mid = (right + left) // 2
        if nums[mid] < nums[left]:
            return self.findMin(nums[:mid + 1])   # keep mid
        else:
            return self.findMin(nums[mid + 1:]) 
        