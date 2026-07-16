class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: Array of temps, where temps[i] represents the dailty temp 
        #       on the ith day
        #output: an array result where result[i] is num of days
        #        after the ith day before a warmer temp appears on a future day
        #        if there is no days then result[i] = 0

        #intution: 
        # for each temp, scan ahead and look for the next hotter day
        # once found, count the steps ahead and append it to that temp
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                resIdx = stack.pop()[1]
                print(resIdx, temp)
                res[resIdx] = i - resIdx
            stack.append((temp, i))
        return res

        
        


        
        