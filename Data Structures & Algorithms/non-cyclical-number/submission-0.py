class Solution:

    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while True:
            t = self.sum_of_squares_of_digits(n)
            if t == 1:
                return True
            elif t in seen:
                return False
            seen.add(t)
            n = t
        
        
        
    def sum_of_squares_of_digits(self, n: int) -> int:

        total = 0
        while n > 0:
            total +=  (n % 10) ** 2
            n //= 10
        return total