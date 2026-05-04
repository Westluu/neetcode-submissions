class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Finding highest frequecies and sorting them 
        #then go to kth idx to get answer

        #so for every distinct num in nums
        #we need to get the frequency count of it
        #then we sort the frequencies
        #go to kth idx to get solution

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #Get Count of each distinct num
        for num in nums:
             count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                res.append(num)

        return res



        

        
        