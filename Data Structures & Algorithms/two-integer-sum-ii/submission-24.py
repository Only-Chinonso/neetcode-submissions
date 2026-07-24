class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                return [res.append(numbers.index(diff) + 1),res.append(numbers.index(num) + 1)]
        return []