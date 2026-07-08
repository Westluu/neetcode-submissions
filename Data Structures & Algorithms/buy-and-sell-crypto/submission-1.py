class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input: An array of ints called prices
        #output: the max profit, where its the max difference between 
        #        prices[idx1] - prices[idx2] where idx1 < idx2
        #        or 0 (which ever is larger)

        #thus it means that idx1 will always be left of idx2
        #so if we split the array in half and find the min and max 
        #on both sides, then using thus we can find the max profit

        l = 0
        r = 1
        max_p = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r+=1
        return max_p
        
        


       
        