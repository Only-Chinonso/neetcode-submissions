class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0,0,0]
        j = 0
        for n in nums:
            if n == 0:
                bucket[0] += 1
            if n == 1:
                bucket[1] += 1
            if n == 2:
                bucket[2] += 1

        for i in range(bucket[0]):
            nums[j] = 0
            j += 1
        for i in  range(bucket[1]):
            nums[j] = 1
            j += 1
        for i in range(bucket[2]):
            nums[j] = 2
            j += 1
        