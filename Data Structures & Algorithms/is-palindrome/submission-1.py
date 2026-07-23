class Solution:
    def isPalindrome(self, s: str) -> bool:
        test = ""
        for cha in s[::-1] :
            test += cha
        if test == s :
            return True
        return False