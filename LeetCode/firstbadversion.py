# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        while start <= end:
            mid = (start + end) // 2
            api_mid = isBadVersion(mid)
            api_prev = isBadVersion(mid-1)
            if api_mid and not api_prev:
                return mid
            elif api_mid:
                end = mid - 1
            else:
                start = mid + 1