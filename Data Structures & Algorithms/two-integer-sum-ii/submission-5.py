class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                res.append(numbers.index(diff))
                res.append(numbers.index(num))
        return res