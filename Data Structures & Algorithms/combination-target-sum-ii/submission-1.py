class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtracking(cur_combination, total, i):
            if total == target:
                res.append(cur_combination.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return

            #include it
            cur_combination.append(candidates[i])
            backtracking(cur_combination, total + candidates[i], i+1)

            #backtrack
            cur_combination.pop()

            #dont include it
            while i < len(candidates) - 1 and candidates[i+1] == candidates[i]:
                i+=1  
            backtracking(cur_combination, total, i+1)

        backtracking([], 0, 0)
        return res
        