class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #input: An array of cost[i] where cost[i] represents the cost to step from the ith step
        #output: The minumum cost to reach the top which is past the last idx which and be translated to len(cost)

        #can choose to start at idx 0 or idx 1
        #from each step we can go up 1 or 2

        #lets first brute force this
        #from the tree we can see that we only care about the min cost from n - 1 and n -2
        #to get to n

        #we can use recursion to get this, however this will take a lot of steps and overlapps thus I DP is a better appraoch here

        #Where DP[i] is the min cost to reach steps i
        #Base Case: DP[0] =0, DP[1] = 0
        #Solution: DP[n + 1]
        #Formula: DP[i] = min(DP[i-1] + cost[i-1], DP[i-2] + cost[i-2])

        prev, cur = 0, 0
        for i in range(2, len(cost) + 1):
            temp = cur
            cur = min(cur + cost[i-1], prev + cost[i-2])
            prev = temp

        return cur

        