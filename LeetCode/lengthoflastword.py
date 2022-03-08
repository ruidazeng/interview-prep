# There's a lot of edge cases for this problem.
# For example, what if there are multiple spaces after last words,
# or what if there if no space after last words, how do I reset?
# Needed to consider all scenarios in order to pass this problem.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_counter = 0
        last_word = 0
        for c in s:
            if c == " " and word_counter != 0:
                last_word = word_counter
                word_counter = 0
            elif c == " ":
                pass
            else:
                word_counter += 1
        
        if word_counter != 0:
            last_word = word_counter
            
        return last_word