class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[-1]
        for n in nums:
            res = min(res,n)
        return res