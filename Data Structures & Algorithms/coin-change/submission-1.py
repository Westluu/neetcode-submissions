class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #input: A list of coins of diff money values
        #and "amount" target amount of money
        #Goal: find the fewest number of coins that make up "amount" 
        # and if not possible return -1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a-c], dp[a])

        print(dp)
        if dp[amount] != amount + 1:
            return dp[amount]

        return -1 


        
