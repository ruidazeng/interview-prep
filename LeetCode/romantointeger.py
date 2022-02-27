class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_MAP = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        prev = 0
        for i in range(1, len(s)+1):
            curr = ROMAN_MAP[s[-i]]
            if curr >= prev:
                total += curr
            else:
                total -= curr
            # update prev
            prev = curr
        return total