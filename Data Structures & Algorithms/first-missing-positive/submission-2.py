class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        e = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in e:
                return num
        return len(nums) + 1