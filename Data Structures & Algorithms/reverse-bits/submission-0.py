class Solution:
    def reverseBits(self, n: int) -> int:
        a = 0
        for i in range(32):
            b = (n >> i) & 1
            a += (b << (31 - i))

        return a
            