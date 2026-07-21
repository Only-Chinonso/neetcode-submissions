class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for cha in s :
            if cha not in t or s.count(cha) != t.count(cha):
                return False
        return True
