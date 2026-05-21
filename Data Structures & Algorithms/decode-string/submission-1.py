class Solution:
    def decodeString(self, s: str) -> str:
        #input: encoded string s
        #output: decoded string 

        #encoding rule: k[encoded_string]
        # str inside squire is being repeated exactly k time
        # k always postive int (so no rational numbers)

        #if int (always followed by square brackets)
        #in brackets only chars then repeated by int before bracket

        #2[a3[b]]c
        # abbbabbac

        #we can use a stack 
        #put items into the stack
        #until the end or if there is closing bracket
        #pop items of the stack then the opening bracket
        #then pop the int for the bracket (then dup the s in the bracket)
        #continue until the str is formed

        stack = []
        stack.append(s[0])
        i = 1
        while stack and i < len(s):
            if s[i] == "]":
                repeat_str = ""
                repeat_char = stack.pop()
                while repeat_char != "[":
                    repeat_str = repeat_char + repeat_str
                    repeat_char = stack.pop()
                
                #repeat the str k times
                k = stack.pop()
                while stack and stack[-1].isdigit():
                    k=stack.pop() + k
                 

                repeat_str=repeat_str*int(k)
                stack.append(repeat_str)

            else:
                stack.append(s[i])
            i+=1
        
       
        result = ""
        for decode in stack:
            result+=decode
        
        return result
                         
            

        
        