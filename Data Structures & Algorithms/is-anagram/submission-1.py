class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = {}
        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 1
        
        for char in t:
            if char in s_freq:
                s_freq[char] -= 1
                if s_freq[char] == 0:
                    del s_freq[char]

        if len(s_freq) == 0:
            return True
        return False
        