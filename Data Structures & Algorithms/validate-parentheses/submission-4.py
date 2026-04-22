class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {')': '(', '}' : '{', ']' : '['}
        stack = []
        for b in s:
            if b in bracket and len(stack) > 0:
                if stack[-1] != bracket[b]:
                    return False
                stack.pop()
            else:
                stack.append(b)
                
        if len(stack) > 0:
           return False 
        return True

        