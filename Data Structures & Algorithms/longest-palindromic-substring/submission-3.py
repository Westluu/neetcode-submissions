class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for i in range(len(s))]
        longest = [(0,0), 1]
        #Base Case (odd len)
        #Plaindrome of 1 char is always True
        for i in range(len(s)):
            dp[i][i] = True
        
        #Base Case (even len)
        #while for plaindrome of len 2, they both have to be equal
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                longest = [(i, i+1), 2]
        
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = length + i - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > longest[1]:
                        longest = [(i,j), length]
        start, end = longest[0]
        return s[start:end+1]

                    




        
        