class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_map = {}
        leftover = []
        arr1_map = {}

        for num in arr2:
            arr1_map[num] = 0

        for num in arr1:
            if num not in arr1_map:
                leftover.append(num)
            else:
                arr1_map[num]+=1
        leftover.sort()
        
        start = 0
        for num in arr2:
            for i in range(start, start + arr1_map[num]):
                arr1[i] = num
            start+=arr1_map[num]

        for i in range(len(leftover)):
            arr1[start+i] = leftover[i]
        return arr1
