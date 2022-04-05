class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = len(columnTitle) - 1
        number = 0
        distance = ord('A') - 1
        for c in columnTitle:
            number += (ord(c) - distance) * 26 ** power
            power -= 1
        return number