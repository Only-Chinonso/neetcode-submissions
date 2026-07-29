class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        SP = [[s,p]for s,p in zip(speed,position)]
        stack = []
        for s,p in SP[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] < stack[-2]:
                stack.pop()
        return len(stack)