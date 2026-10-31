class Solution:
    def isAnagram(self, t1: str, t2: str) -> bool:
        
        if len(t1) != len(t2):
            return False

        count = [0] * 26
        for char in t1:
            count[ord(char) % 26] += 1
        
        for char in t2:
            i = ord(char) % 26
            if count[i] == 0:
                return False
            else:
                count[i] -= 1
        
        return True