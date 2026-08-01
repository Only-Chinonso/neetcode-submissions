class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums) - 1
        res = nums[0]
        if nums[l] < nums[r]:
             return nums[l]
        while l <= r:
            m = (r + l) // 2
            res = min(res,nums[m],nums[r],num[l])
            if nums[l] < nums[m]:
                l = m + 1
            elif nums[l] > nums[m]:
                r = m 
            else:
                r = l - 1
        return res
        