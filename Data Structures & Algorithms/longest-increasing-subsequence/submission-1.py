class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hashmap = {}
        best = 0
        for num in nums:
            best = 1
            for b in hashmap:
                if b < num:
                    best = max(best,hashmap[b] + 1)
            hashmap[num] = best
        return max(hashmap.values())

