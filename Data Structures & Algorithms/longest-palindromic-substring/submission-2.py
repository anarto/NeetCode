class Solution:
    def longestPalindrome(self, t: str) -> str:

        n = len(t)
        a = ""
        len_a = 0

        for i in range(n):
            
            left, right = i, i

            while left >= 0 and right < n and t[left] == t[right]:
                # print(f"[odd] i = {i}, right - left + 1 ={right - left + 1}, len_a = {len_a}, t[left:right + 1]= { t[left:right + 1]}, check= {(right - left + 1) > len_a}")
                if (right - left + 1) > len_a:
                    a = t[left: right + 1]
                    len_a = right - left + 1
                left -= 1
                right += 1

            left, right = i, i + 1

            while left >= 0 and right < n and t[left] == t[right]:
                # print(f"[even] i = {i}, right - left + 1 ={right - left + 1}, len_a = {len_a}, t[left:right + 1]= { t[left:right + 1]}, check= {(right - left + 1) > len_a}")
                if (right - left + 1) > len_a:
                    a = t[left: right + 1]
                    len_a = right - left + 1
                left -= 1
                right += 1
        
        
        return a