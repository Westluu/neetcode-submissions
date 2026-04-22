class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_table = {}
        for i,v in enumerate(nums):
            lookup = target - v
            if lookup in lookup_table:
                return [min(i, lookup_table[lookup]), max(i, lookup_table[lookup])]
            else:
                lookup_table[v] = i
        
        return [-1, -1]