# Newton's Method: https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r * r > num:
            r = (r + num/r) //2
        return r * r == num