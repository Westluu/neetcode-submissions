class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #array sorted, given a target
        #output: idx1 and idx2 such that idx1 < idx2 and they add up to target. idx1 != idx2

        #since idx1 and idx2 cannot be equal, I believe 2 pointer is the best algo to traverse the list

        l = 0
        r = len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l+=1
            else:
                r-=1
        return -1


        