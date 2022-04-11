class Solution:
    def hammingWeight(self, n: int) -> int:
        hamming_weight = 0
        while n:
            hamming_weight += n & 1
            n >>= 1
        return hamming_weight
    
    
# Faster Solution (also using bit manipulation)
# n & (n-1) drops the lowest set bit
# Simply count the number of operations for the number of ones
# =========================================================
# class Solution:
#     def hammingWeight(self, n):
#         hamming_weight = 0
#         while n:
#             n &= (n-1)
#             hamming_weight += 1
#         return hamming_weight