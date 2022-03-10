# Newton-Raphson method
# Uses binary search to reduce search space
# Time complexity O(log N) instead of O(N)

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x//2
        
        # special cases for square roots
        if x == 0 or x == 1:
            return x
        
        while left <= right:
            midpoint = (left + right) // 2
            if midpoint * midpoint == x:
                return midpoint
            elif midpoint * midpoint > x:
                right = midpoint - 1
            else:
                answer = midpoint
                left = midpoint + 1
        
        return answer