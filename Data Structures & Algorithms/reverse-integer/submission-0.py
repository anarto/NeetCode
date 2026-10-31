class Solution:
    def reverse(self, x: int) -> int:
        
        is_negative = x < 0
        r = 0
        x = abs(x)
        while x > 0:
            r = (r * 10) + (x % 10)
            x //= 10
        if r > 2 ** 31 or (is_negative and r > 2 ** 31 - 1):
            return 0
        return -r if is_negative else r 