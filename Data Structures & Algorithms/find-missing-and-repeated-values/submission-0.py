class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = 0
        b = 0
        for l in grid:
            for n in l:
                if n in seen:
                    dup = n
                seen.add(n)
        for n in range(1,(len(grid)**2) + 1):
            if n not in seen:
                b = n
        return [a,b]