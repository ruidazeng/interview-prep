class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haystack_size = len(haystack)
        needle_size = len(needle)
        
        # special cases
        if needle == "":
            return 0
               
        for i in range(haystack_size):
            if haystack[i:i+needle_size] == needle:
                return i
            
        return -1