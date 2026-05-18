class Solution:
    def isValid(self, s: str) -> bool:
        #input: a string containing brackets
        
        #output: True, if string is valid
        # a string is valid if every open bracket is closed 
        # by the same bracket and closed in correct order

        # [(])
        # [
        # (
        # ] -> false 

        #pattern:
            #ordering matters, opening brackets requires closing
            #if they are nested then first brackets or closed last
            # LIFO 
            # stack
        
        # ([{}])
        #having a mapping from closing to opening
        bracket_map = { ']':'[', ')': '(', '}':'{' } 

        stack = [] #will only include bracket
        for char in s:
            #if we hit a closed bracket
            if char in bracket_map and len(stack) > 0:
                if stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack) > 0:
            return False
        return True


        