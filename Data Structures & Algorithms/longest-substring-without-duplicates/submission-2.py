class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        window_set = set()
        longest_substring = 0
        while end < len(s):
            if s[end] not in window_set:
                window_set.add(s[end])
                end += 1
                longest_substring = max(longest_substring, end - start)
            else:
                window_set.remove(s[start])
                start += 1
        return longest_substring
        

        