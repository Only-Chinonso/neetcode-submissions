class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0 and s[0].isalpha():
            return 1
        if len(s) == 0:
            return 0
        r = len(s) -1 
        res = 0
        while s != 0 and not s[r].isalpha():
            r -= 1
        l = r
        while l != 0 and s[l].isalpha():
            res += 1
            l -= 1
        return res