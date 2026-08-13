class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtracking(path, i):
            if i >= len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            backtracking(path, i+1)

            path.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            backtracking(path, i+1)
        backtracking([], 0)
        return res
            
        