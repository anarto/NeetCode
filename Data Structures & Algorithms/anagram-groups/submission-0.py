class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char) % 26] += 1

            k = tuple(count)
            if k in anagrams:
                anagrams[k].append(word)
            else:
                anagrams[k] = [word]

        return list(anagrams.values())