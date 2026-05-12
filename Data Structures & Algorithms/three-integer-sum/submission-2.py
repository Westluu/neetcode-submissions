class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                diff = nums[i] + nums[left] + nums[right]
                if diff == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                elif diff > 0:
                    right-= 1
                else:
                    left+=1 

        return res
        