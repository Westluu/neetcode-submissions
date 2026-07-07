class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #input: 2 strs 
        #output: return T if both strs are anagrams else return F

        #Anagram by definition is a string that contains the exact chars
        #as another string but ordering does not matter

        #Then if 2 strings have the same frequency of chars then by definition
        #they are anagrams of each other

        #so we can solve this by getting the frequency count of each str
        #then compare to determine if they are anagrams are not

        if len(s) < len(t) or len(t) < len(s):
            return False
        
        s_map = {}
        t_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
        
        if s_map == t_map:
            return True
        return False




        