class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Return modified string.
        """
        VOWELS = "aeiouAEIOU"
        # two pointers approach
        start = 0
        end = len(s) - 1
        new_str = list(s)
        
        while start < end:
            if new_str[start] not in VOWELS:
                start += 1
            elif new_str[end] not in VOWELS:
                end -= 1
            else:
                new_str[start], new_str[end] = new_str[end], new_str[start]
                start += 1
                end -= 1

        return "".join(new_str)