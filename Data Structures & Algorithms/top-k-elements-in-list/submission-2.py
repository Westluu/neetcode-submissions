class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input: nums a list of intergers and K an integer
        #output: return the k most frequent elements
        k_freq_elements = []
        count_map = defaultdict(int)
        freq_array = []
        for i in range(len(nums) + 1):
            freq_array.append([])

        #1st pass getting count
        for num in nums:
            count_map[num]+=1
        
        #pass 2 loop the map and place it via on the freq array
        for num, count in count_map.items():
            freq_array[count].append(num)
        
        #go backwards to get most frequent k element
        for i in range(len(freq_array)-1, -1, -1):
            if len(freq_array) > 0:
                for num in freq_array[i]:
                    k_freq_elements.append(num)
                    if len(k_freq_elements) == k:
                        return k_freq_elements

        return -1
                 

