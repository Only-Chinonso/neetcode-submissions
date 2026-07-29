class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r,l = 0,len(nums) - 1
        m = (l + r) // 2
        while l >= r:
            if nums[m] > target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
            else:
                return m
        return -1