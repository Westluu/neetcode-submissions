class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, num in enumerate(nums):
            #continue if number is postive (no point in checking)
            if num > 0:
                break
            
            #if its a duplicate skip it
            if idx > 0 and num == nums[idx-1]:
                continue
            
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                
                #sum is too big, reduce biggest num
                if threeSum > 0:
                    r-=1
                
                #sum too small, inscrease smallest num
                elif threeSum < 0:
                    l+=1
                
                #its zero, found the result
                else:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res



