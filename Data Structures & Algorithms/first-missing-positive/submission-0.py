class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums.sort()

        n = 1
        for num in nums:
            if num == n:
                n += 1
            elif num > n:
                break
        return n