class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = sorted(s)
        cnt = 0
        l = set()
        for i,cha in enumerate(s) :
            l.append(cha)
            if s[i] != s[i - 1] and ord(cha) == ord(s[i + 1]) - 1 and cha not in l:
                cnt += 1
            l.append(cha)
        return cnt
