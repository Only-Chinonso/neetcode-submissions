class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 # left pointer
        chaset = set()# to store characters 
        res = 0 #the longest substring
        for r in range(len(s)): # r = right pointer
            while s[r] in chaset :#checking if chr is in set
                chaset.remove(s[l])#shicking set on till the chr is no more in set
                l += 1
            chaset.add(s[r])#storing it in set 
            res = max(res,r - l + 1)# assigning res to the biggest between the current res and the new res
        return res 
