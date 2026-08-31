class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for i in range(len(s))]
        res = 0
    
        #Base Case
        for i in range(len(s)):
            dp[i][i] = True
            res+=1
        
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res+=1
        
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    res+=1
        
        return res
        

