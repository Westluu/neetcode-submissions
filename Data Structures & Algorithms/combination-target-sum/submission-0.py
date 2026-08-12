class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(cur_combination, total, i):
            if total == target:
                res.append(cur_combination.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            #include it
            cur_combination.append(nums[i])
            backtracking(cur_combination, total + nums[i], i)

            #backtrack
            cur_combination.pop()

            #skip it
            backtracking(cur_combination, total, i+1)
        
        backtracking([], 0, 0)
        return res


        