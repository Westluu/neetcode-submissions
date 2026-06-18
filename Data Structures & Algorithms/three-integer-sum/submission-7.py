class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            #if its postive skip it 
            if nums[i] > 0:
                break
            
            #skip duplicates
            while i<len(nums) and i > 0 and nums[i] == nums[i-1]:
                i+=1
            
            #2SUM
            l, r = i+1, len(nums) - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target > 0:
                    r-=1
                elif target < 0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
            i+=1
        return res
            

            



            

       

