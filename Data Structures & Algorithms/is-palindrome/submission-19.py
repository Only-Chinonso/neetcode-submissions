class Solution:
    def isPalindrome(self, s: str) -> bool:
        comp = ""
        for cha in s :
            if cha.isalnum():
                comp += cha
        return comp.lower() == comp[::-1].lower()