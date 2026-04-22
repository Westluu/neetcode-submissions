class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - ord('a')] += 1
            if tuple(key) in anagram_map:
                anagram_map[tuple(key)].append(s)
            else:
                anagram_map[tuple(key)] = [s]
        
        result = []
        for key in anagram_map:
            result.append(anagram_map[key])
        return result

                
        