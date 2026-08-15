class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = 0
        for i in range(numbers):
            while j+1 < len(numbers) and numbers[j] == numbers[j+1]:
                j += 1
            cur_sum = numbers[i] + numbers[j+1]
            if cur_sum == target:
                return [numbers[i],numbers[j+1]]
            j = i