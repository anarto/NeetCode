class Solution:
    def countSubstrings(self, t: str) -> int:
        
        count = 0

        n = len(t)
        for i in range(n):

            l, r = i, i

            while l >= 0 and r < n and t[l] == t[r]:
                count += 1
                l -= 1
                r += 1

            
            l, r = i, i + 1

            while l >= 0 and r < n and t[l] == t[r]:
                count += 1
                l -= 1
                r += 1

        return count