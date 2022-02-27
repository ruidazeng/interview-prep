class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = [nums[0]]
        curIndex = 1
        for num in nums[1:]:
            if target - num in tracker:
                return [nums.index(target-num), curIndex]
            else:
                tracker.append(num)
            curIndex += 1
            
