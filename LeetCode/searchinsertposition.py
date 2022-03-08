class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        midpoint = length // 2
        
        left = 0
        right = len(nums)
        
        while left < right:
            midpoint = (right + left) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint
        return left