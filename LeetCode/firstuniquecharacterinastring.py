class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_cnt = dict()
        for i in range(len(s)):
            c = s[i]
            if  c in char_cnt:
                char_cnt[c] += 1
            else:
                char_cnt[c] = 1
        # now find non-repeat
        for i in range(len(s)):
            c = s[i]
            if char_cnt[c] == 1:
                return i
        return -1