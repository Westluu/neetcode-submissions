class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        #freq count of window
        #continue window while freq count size is 1 + k
        #if it overfills, move start window in until freq count size is 1 + k
        #keep track of longest window size

        start = end = 0
        freq_count = {}
        max_freq = 0
        longest_dup = 0

        while end < len(s):
            freq_count[s[end]] = freq_count.get(s[end], 0) + 1
            max_freq = max(max_freq, freq_count[s[end]])
            while (end - start + 1) - max_freq > k:
                freq_count[s[start]] -= 1
                start += 1
            longest_dup = max(longest_dup, end - start + 1)
            end += 1
        return longest_dup    


        