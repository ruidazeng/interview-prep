class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        slow_pointer = 0
        
        for fast_pointer in range(n):
            if nums[slow_pointer] != nums[fast_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]
        
        # convert index into array size
        return slow_pointer+1
                