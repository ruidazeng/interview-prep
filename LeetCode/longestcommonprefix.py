class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Approach 2: Vertical scanning
        """
        if (strs == None or len(strs) == 0):
            return ""
        # longest prefix must be shorter than length of the first string
        ans = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return ans
            ans += c
        return ans