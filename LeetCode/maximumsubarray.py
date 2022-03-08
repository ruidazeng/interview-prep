class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        slow_pointer = 0
        fast_pointer = 0
        max_sum = 0
        cur_sum = 0
        prev_sum = 0
        n = len(nums)
        
        while slow_pointer < n:
            cur_sum += nums[fast_pointer] 
            
            # update counters
            if cur_sum < prev_sum:
                cur_sum -= nums[slow_pointer]
                slow_pointer += 1
            if cur_sum > max_sum:
                max_sum = cur_sum

            # move on
            prev_sum = cur_sum
            if fast_pointer < n-1:
                fast_pointer += 1
            
            print(slow_pointer, fast_pointer, cur_sum, prev_sum, max_sum)
        
        return max_sum
        