class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) -1 
        res = 0
        while s != 0 and not s[r].isalpha():
            r -= 1
        l = r
        while l != 0 and s[l].isalpha():
            res += 1
            l -= 1
        return res