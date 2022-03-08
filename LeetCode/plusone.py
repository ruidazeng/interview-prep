class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        if digits[n] != 9:
            digits[n] += 1
        else:
            while n >= 0:
                if digits[n] == 9:
                    digits[n] = 0
                    # additional clause for [9] and [1, 0]
                    if n == 0:
                        digits.insert(0, 1)
                else:
                    digits[n] += 1
                    break
                
                n -= 1
        
        return digits
            