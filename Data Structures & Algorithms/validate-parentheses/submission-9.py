class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = { ']':'[', ')': '(', '}':'{' }
        for char in s:
            if char in bracket_map: 
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
    
        if len(stack) == 0:
            return True
        return False        