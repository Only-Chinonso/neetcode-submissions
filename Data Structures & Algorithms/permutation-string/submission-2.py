class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1)):
            if r - l + 1 > len(s2):
                l += 1
            if  r - l + 1 == len(s2):
                if sorted(s1[l : r + 1]) == sorted(s2):
                    return True
        return False