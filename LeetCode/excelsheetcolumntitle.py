class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        distance = ord('A')
        while columnNumber > 0:
            # adjustment for distance
            letter = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            result = chr(letter+distance) + result
        return result