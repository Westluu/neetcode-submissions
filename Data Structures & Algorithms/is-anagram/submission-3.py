class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        for i in range(n):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        return s_count == t_count


        