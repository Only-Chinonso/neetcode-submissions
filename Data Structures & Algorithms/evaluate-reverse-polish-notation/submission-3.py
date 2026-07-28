class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch.isdigit():
                stack.append(int(ch))
            if ch == "*":
                sm = 1
                for n in stack :
                    sm *= n
                while stack:
                    stack.pop()
                stack.append(sm)
            if ch == "+":
                sm = sum(stack)
                while stack:
                    stack.pop()
                stack.append(sm)
            if ch == "-":
                sm = stack[0]
                for i in range(1,len(stack)):
                    sm -= stack[i]
                while stack:
                    stack.pop()
                stack.append(sm)
        return stack[0] if stack else 0