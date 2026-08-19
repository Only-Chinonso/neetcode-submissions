class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = sum(nums)
        cur = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] <= 0 and cur <= 0:
                cur *= nums[i]
            elif nums[i] <= 0:
                cur = nums[i]
            elif nums[i] > 0 and cur <= 0:
                cur = nums[i]
            else:
                cur *= nums[i]

            res = max(res,cur)
            i += 1
        return res