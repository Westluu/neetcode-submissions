class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input: An array of ints called nums
        #output: the len of the longest consecutive sequence 
        #        that can be formed in nums

        # consecutive sequence by definition is a sequence where 
        # elements are exactly one greater than the previous and 
        # they dont have to the contiguous in the array. Array is modifiable

        # since we are looking for sequences that are exactly 1 greater
        # intution there are 2 ways (sort and find sequence) or 
        # (create a set and look for sequences)
        # sort would be 2 passes (sort then check each element and its right and form the sequence)
        # time complexity: o(nlogn), space: o(1)

        # while the create set and lookup
        # 2 passes as well, build the lookup set and go through elements and find its sequence
        # time complex: o(n), space: o(n)

        num_lookup = set()
        for num in nums:
            num_lookup.add(num)
        
        max_len = 0
        for num in nums:
            if num - 1 not in num_lookup:
                cur_len = 1
                while num + cur_len in num_lookup:
                    cur_len+=1
                max_len = max(max_len, cur_len)
        return max_len

            