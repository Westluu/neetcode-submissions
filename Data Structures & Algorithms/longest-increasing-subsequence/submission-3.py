class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #input: array of ints
        #output: longest increasing subsequence

        #by def an subsequences is a sequences 
        #from the given input by removing some or not element
        #along without changing the ordering of the sequence

        #thus by def an increasing sequence is an sequence where 
        #the order of the sequence is stricitly increasing

        # [9,1,4,2,3,3,7]
        # 9, 1 (x)
        # 1, 4, (2)
        # 1, 2, 3 (3)
        # 1, 2, 3, 7 (4)

        # [1,1,2,2,3,3,4]


        #pattern is choices (between choosing the next element or the one after)
        #tries, backtracking
        #we are looking for optimal solution and not all possible
        #DP problem best approach

      #Def: LIS[i] = Is an array that holds the longest increasing sequence at index i
        #Base Case: LIS[0] = 1
        #Solution: LIS[n]
        #Formula: LIS[i] = max(LIS[i], (check all prev vals if increasing (LIS[prev] + 1) else 1) )
        n = len(nums)
        LIS = [1] * n
        LIS[0] = 1
        maxLIS = 1
        for i in range(1, n):
            for prev in range(0, i):
                if nums[i] > nums[prev]:
                    LIS[i] = max(LIS[i], LIS[prev] + 1)
                maxLIS = max(maxLIS, LIS[i])
        return maxLIS