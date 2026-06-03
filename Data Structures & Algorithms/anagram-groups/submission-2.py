class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input: strs is an array of strings
        #outputs: A list of list where each list contains strings that are anagrams of each other

        #edge cases: is the anagram empty, empty?

        #Def Anagram: Is a string that contains that exact same characters as another strings
        #thus by definition 2 strings are anagrams of each other if they have the same freq count of char

        #Data Structure: A an array of placeholder 0 containing ascii value

        #so for each string, we get the frequency count and then store that count as a key in a hash map

        anagram_map = defaultdict(list)
        freq_array = [0] * 26

        for string in strs:
            for char in string:
                freq_array[ord(char) - ord('a')] += 1
            key = tuple(freq_array)
            anagram_map[key].append(string)
            freq_array = [0] * 26
        
        return list(anagram_map.values())

