class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in hashset:
                return [hashmap[diff],hashmap[num]]
            hashmap[num] = i