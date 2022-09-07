# https://docs.python.org/3/library/functions.html#bin
# bin(): convert an integer number to a binary string prefixed with “0b”

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ["{:d}:{:02d}".format(h, m)
                    for h in range(12) for m in range(60)
                    if (bin(h) + bin(m)).count('1') == turnedOn]