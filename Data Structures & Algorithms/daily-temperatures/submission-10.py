class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackt,stackint = stack.pop()
                res[stackint] = i - stackint
            stack.append((t,i))
        return res