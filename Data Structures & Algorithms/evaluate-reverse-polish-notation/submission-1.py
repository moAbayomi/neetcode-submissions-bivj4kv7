class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif t == '-':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(b - a)
            elif t == '/':
                a, b = int(stack.pop()), int(stack.pop())
                stack.append(int(b / a))
            elif t == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            else:
                stack.append(int(t))
        
        return stack[0]
        