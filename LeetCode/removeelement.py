class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        slow_pointer = 0
        
        for fast_pointer in range(n):
            if nums[fast_pointer] != val:
                nums[slow_pointer] = nums[fast_pointer]
                slow_pointer += 1
        
        # slow_pointer is ahead by one
        return slow_pointer
        