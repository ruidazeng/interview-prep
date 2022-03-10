# This is a representation of the Fibonacci series
# We notice that the solution for distinct ways to climb
# is a result of taking 2 steps from the (n-2)th block,
# or by taking 1 step from (n-1)th block.

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        # python tuple assignment, syntatic sugar
        for i in range(n):
            # essentially Fibonacci's number
            a, b = b, a + b
        return a