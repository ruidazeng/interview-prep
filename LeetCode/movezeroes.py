class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pointer] = nums[zero_pointer], nums[i]
                # increment by one to ensure that zero_pointer will always stay ahead of all zeroes
                zero_pointer += 1