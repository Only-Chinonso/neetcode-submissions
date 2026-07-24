class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for n in nums :
            if n - 1 not in nums:
                length = 0 
                while n + length in num:
                    length += 1
                longest = max(longest,length)
        return longest