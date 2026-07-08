class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input: A str called s
        #output: the len of the longest substring of s
        #        without duplicate chars

        #intution: we using sliding window and grow the window
        # then use a set to check for duplicate chars in the substring
        # time compl: o(n), space compl: o(n)
        longest_substring = 0
        l = 0
        substring_set = set()

        for r in range(len(s)):
            while s[r] in substring_set:
                substring_set.remove(s[l])
                l+=1
            substring_set.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
        return longest_substring



            

       
            
        