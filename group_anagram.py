from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:  # Changed variable name from str to word
            count = self.helper(word)
            current = anagram_map.get(count, [])
            current.append(word)
            anagram_map[count] = current
        
        return list(anagram_map.values())  # Convert dict_values to a list

    def helper(self, word: str):
        arr = [0] * 26  # Frequency array for 26 lowercase letters
        for char in word:
            index = ord(char) - ord('a')
            arr[index] += 1
        
        return tuple(arr)  # Use tuple instead of str(arr)

