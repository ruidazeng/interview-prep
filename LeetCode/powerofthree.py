# Check to see if log10(n) / log10(3) returns an int...
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Note that logarithmic of negative/zero is undefined in mathematics
        if n <= 0:
            return False
        res = math.log10(n) / math.log10(3)
        return int(res) == res