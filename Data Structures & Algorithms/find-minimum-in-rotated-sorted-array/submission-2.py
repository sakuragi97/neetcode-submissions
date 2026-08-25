class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0 , len(nums)-1
        mid = (right-left) // 2
        while left < right:
            if nums[right] > nums[left]:
                return nums[left]        
            if nums[mid] < nums[left]:
                right = mid
                mid = left +(right-left) // 2
            else:
                left = mid + 1
                mid = left + (right-left) // 2
        return nums[mid]