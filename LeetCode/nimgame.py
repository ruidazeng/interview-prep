class Solution:
    # f(x - 4) is a critical point, if f(x-4) is false, then f(x) will be always false
    # Initial conditions, f(1), f(2), f(3) will be true (A always win), and f(4) will be false
    def canWinNim(self, n: int) -> bool:
        return (n % 4 != 0)