class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        count = 0
        for i in range(1, n+1):
            count = i%2 + ans[int(i/2)]
            ans.append(count)
        return ans