class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input: An array of ints called nums and int called k
        #output: return an array of ints of the k most frequent elements in nums
        #        the array can be in any order

        # get the frequency count of each element
        # determine the frequency count ordering and sort it
        # get the k most frequent element

        freq_count = {}
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1

        freq_order = [[] for i in range(len(nums))]
        for num, freq in freq_count.items():
            print(freq)
            freq_order[freq - 1].append(num)
        
        k_elements = []
        for i in range(len(freq_order) - 1, -1, -1):
            if len(freq_order[i]) == 0:
                continue
            else:
                for freq in freq_order[i]:
                    k_elements.append(freq)
                    if len(k_elements) == k:
                        return k_elements
        


        
        
        






