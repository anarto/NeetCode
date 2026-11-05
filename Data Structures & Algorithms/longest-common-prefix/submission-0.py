class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if (len(strs) == 1):
            return strs[0]
        
        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]
            if len(word) < len(prefix):
                word, prefix = prefix, word

            for j in range(len(prefix)):
                if prefix[j] != word[j]:
                    prefix = prefix[0:j]
                    break

        return prefix


