class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0 for _ in range(26)]
        for mag in magazine:
            cnt[ord(mag)-ord('a')] += 1
        for rans in ransomNote:
            cnt[ord(rans)-ord('a')] -= 1  
            if cnt[ord(rans)-ord('a')] < 0:
                return False
        return True