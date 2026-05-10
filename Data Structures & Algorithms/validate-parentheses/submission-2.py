class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracs = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for br in s:
            if br in ['[', '{', '(']:
                stack.append(br)
            elif br in [']', '}', ')']:
                if len(stack) > 0 and stack[len(stack) - 1] == bracs[br]:
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False
        return True

        