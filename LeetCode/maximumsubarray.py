# The problem was originally proposed by Ulf Grenander of Brown University in 1977,
# as a simplified model for maximum likelihood estimation of patterns in digitized images.

# This solution is also known as Kadane's Algorithm.
# It is linear time algorithm. This solution is given by Joseph B. Kadane in late '70s.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        
        for i in range(1, len(nums)):          
            cur_sum += nums[i]
            if cur_sum < nums[i]:
                cur_sum = nums[i]
            
            # update max
            if cur_sum > max_sum:
                max_sum = cur_sum
                
        return max_sum