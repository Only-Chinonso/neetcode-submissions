class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        l = (len(nums) - 1) // 2
        while nums[l] != target :
            if target > nums[l]:
                l += (len(nums) - l) // 2
            else:
                l -= (len(nums) - l) // 2
        return l