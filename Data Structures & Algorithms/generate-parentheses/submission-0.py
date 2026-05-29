class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #input: An int n
        #output: An array of well-formed parentheses strings that I can generate with 
        #using n pairs of parentheses

        #Getting all permutations of a problem
        #Alogrithm is backtracking problem

        #By definition well-formed para. str is a string where each 
        #open parentheses, there exist a closing parenthese for that opening 
        
        #n = 1 ()
        #[()]
        
        #n = 3
        #[()]

        sol = []
        res = []

        def backtracking(openP, closeP):
            #if used up all n paratheses
            if openP == closeP == n:
                res.append("".join(sol))
                return

            #go left add more open parantheses
            if openP < n:
                sol.append("(")
                backtracking(openP + 1, closeP)
                sol.pop()

            #go right add more close parantheses
            if closeP < openP:
                sol.append(")")
                backtracking(openP, closeP + 1)
                sol.pop()
        
        backtracking(0, 0)
        return res