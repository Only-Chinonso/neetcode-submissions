class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}#{cha:count}
        l = 0 #left
        res = 0
        for r in range(len(s)) :#r = right pointer that start at the left and go all way to the right 
            count[s[r]] = count.get(s[r],0) + 1 # adding 1 to the count of the cha we are on
            if (r - l + 1) - max(count.values()) > k:#checking if the number that we need do replace have pass k
                count[s[l]] -= 1#if there are we would subtract the count of the cha by 1
                l += 1#then we will move the left pointer by 1
            res = max(res,r - l + 1)#assign res to the biggest number between the old res and the length of the window that we are on 
        return res