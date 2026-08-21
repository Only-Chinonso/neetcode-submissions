class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            for b in hashmap:
                if b < num:
                    hashmap[num] = hashmap.get(hashmap[b]) + 1
            if num not in hashmap:
                hashmap[num] = 1
        return max(hashmap.values())

