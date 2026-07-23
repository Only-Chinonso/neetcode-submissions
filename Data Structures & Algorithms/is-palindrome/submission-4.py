class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for cha in s :
            if cha.isalnum():
                cleaned += cha
        return cleaned.lower() == cleaned[::-1].lower()