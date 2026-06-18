class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #since we can form the sequence
        #and we only care about sequence where its exactly > 1
        #then creating a set to look for the next number is very efficent

        #we makes nums a set
        #check for start of sequence
        #then continue sequence until end
        #record max_size
        #return

        set_num = set()
        max_size = 0
        for num in nums:
            set_num.add(num)

        for num in set_num:
            if num - 1 not in set_num:
                size = 1
                while num + size in set_num:
                    size+=1
                max_size = max(max_size, size)

        return max_size         