class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #input: string s and array wordDict that contain strings
        #output: T if s can be segmnted into space-seperated squence using wordDict strings
        #else F

        # neetcode, [neet, code]
        # neet code T

        #applepenapple [apple, pen, ape]
        #apple pen apple T

        #catsincars [cats, cat, sin, in, car]
        #cats in car [s] F
        #cat sin car [s] F

        #dp[i]: represets if the a word can be broken up at idx i
        #dp[0] = True, as empty string can be broken into nothing
        #dp[i] = dp[i + len(w)]
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and s[start: i] == w and dp[start]:
                    dp[i] = True
                    break

        return dp[len(s)]
    

        


