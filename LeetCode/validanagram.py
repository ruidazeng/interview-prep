class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = dict()
        for c1 in s:
            if c1 in tracker:
                tracker[c1] += 1
            else:
                tracker[c1] = 1
        
        for c2 in t:
            if c2 in tracker:
                tracker[c2] -= 1
            else:
                return False
        
        for c3 in tracker:
            if tracker[c3] != 0:
                return False
        
        return True