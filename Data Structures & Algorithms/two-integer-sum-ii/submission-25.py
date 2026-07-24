class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for num in numbers:
            diff = target - num
            if diff in numbers:
                return [numbers.index(diff) + 1, numbers.index(num) + 1]
        return []