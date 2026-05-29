class Solution:
    def firstUniqChar(self, s: str) -> int:
        #2 passes
        #pass 1 make frequency count, 
        #pass 2 go through str and return first idx with 0 frequencies

        countMap = {}
        for char in s:
            countMap[char] = countMap.get(char, 0) + 1

        for i in range(len(s)):
            if countMap[s[i]] == 1:
                return i
            i+=1
        return -1


        