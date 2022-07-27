class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        n = len(s)
        while i < len(s)/2:
            # swap front and back
            front = s[i]
            back = s[n-1-i]
            s[i] = back
            s[n-1-i] = front
            # move onto next element
            i += 1