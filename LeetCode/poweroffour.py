import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return int(math.log10(n)/math.log10(4)) == math.log10(n)/math.log10(4)