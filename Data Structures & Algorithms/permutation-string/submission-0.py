class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(L1)):
            if r - l + 1 > len(L2):
                l += 1
            if  r - l + 1 == len(L2):
                if sorted(L1[l : r + 1]) == sorted(L2):
                    return True
        return False