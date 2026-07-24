class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = []
        for num in numbers:
            diff = target - num
            if diff in numbers:
                n.append(numbers.index(diff), numbers.index(num))
                for num in n :
                    res.append(num)
        return res