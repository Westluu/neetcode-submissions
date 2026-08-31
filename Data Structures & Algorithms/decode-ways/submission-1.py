class Solution:
    def numDecodings(self, s: str) -> int:
        #mapping int chars to English Alpha
        #int chars go from 0 - 26 with mapping (A-Z) based on order
        #solution: find total number of ways to decode the str

        # looking for best solution, and since 10 can
        # decoded as 1 - A or 10 - J, makes me think its a DP problem

        # Example: 1012
        # 10 1 2
        # 10 12

        #0 maybe be an edge case (as there is no 0 mapping)

        #mapping ints is at most 2 digits with range (1-26)
        #have to use all digits cannot skip
        #so we can check 2 digits (check if there exist a 0)
        #if not increase total by 2
        if s[0] == "0":
            return 0
            
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            one = int(s[i-1])
            two = int(s[i-2:i])

            if 1 <= one <= 9:
                dp[i] += dp[i-1]
            
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
            
        return dp[len(s)]


