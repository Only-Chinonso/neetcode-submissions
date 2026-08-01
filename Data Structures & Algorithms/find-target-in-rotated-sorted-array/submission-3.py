class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums) - 1
        while l <= r:
            m = (r + l) // 2
            if nums[l] <= nums[m]:
                r = len(nums) - 1
                if target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                r = m - 1
        return m

        