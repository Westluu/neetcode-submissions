class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input: An array of nums
        #output: T if any dup appears and F if there no duplicates
        
        #loop through the array while keeping track of past elements 
        #can for each loop check if it exist, if it does return True
        #keep looping until the end
        #then return False

        #we can use a set of keeping track for fast lookup

        past_nums = set()
        for num in nums:
            if num in past_nums:
                return True
            past_nums.add(num)
        return False



        