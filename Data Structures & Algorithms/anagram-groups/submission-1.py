class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #By definition an Anagram is if a str contains same chars as another string
        #but order can be different

        #Then by definition if 2 strings are anagrams then it must mean that they have
        #the same frequencies/count of chars

        #So it must mean that a group of anagrams all have the same frequency count

        #So we can group anagrams in a Map using the frequency as a key

        anagram_map = defaultdict(list)
        for string in strs:
            freq = [0] * 26 #only eng letters 

            #get the freq map
            for char in string:
                rank = ord(char) - ord('a')
                freq[rank]+=1
            
            #map by freq/counts
            anagram_map[tuple(freq)].append(string)

        return list(anagram_map.values())



            
