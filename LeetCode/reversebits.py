class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for _ in range(32):
            # left shift out by 1, use & operand to find the last digit of n
            # if last digit is 0, 0 & 1 = 0, if last digit is 1, 1 & 1 = 0
            # other digits do not matter since 0 & 0 = 0 and 1 & 0 = 1 for the remaining bits
            out = (out << 1) + (n & 1)
            # right shift n, i.e. drop the most significant bit, since we already added it
            n >>= 1
        return out
        