# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        
        if len(s1) > len(s2): return False

        c1, c2 = [0] * 26, [0] * 26
        for index in range(len(s1)):
            c1[ord(s1[index]) % 26] += 1
            c2[ord(s2[index]) % 26] += 1

        matches = 0
        for i in range(26):
            matches += (1 if c1[i] == c2[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            i = ord(s2[r]) % 26
            c2[i] += 1
            if c2[i] == c1[i]:
                matches += 1
            elif c2[i] == c1[i] + 1:
                matches -= 1

            i = ord(s2[l]) % 26
            c2[i] -= 1
            if c2[i] == c1[i]:
                matches += 1       
            elif c2[i] == c1[i] - 1:
                matches -= 1    
            l += 1
            
        return matches == 26


        