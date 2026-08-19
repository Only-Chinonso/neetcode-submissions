class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res,cur = nums[0],1
        i = 0
        while i < len(nums):
            if nums[i] <= 0:
                cur = 0
            else:
                cur *= nums[i]
            res = max(res,cur)
        return res