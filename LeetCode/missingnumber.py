class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        
        count = len(nums)
        expected = int(count * (count + 1) / 2)
        return expected - total
            
        