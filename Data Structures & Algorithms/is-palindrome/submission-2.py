class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for cha in s :
            if cha.alnum():
                cleaned += cha
        return cleaned == cleaned[::-1]