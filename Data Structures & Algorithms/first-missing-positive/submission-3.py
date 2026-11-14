class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        
        print(nums)
        for num in nums:
            if 1 <= abs(num) <= n:
                i = abs(num) - 1
                if nums[i] > 0:
                    nums[i] *= -1
                elif nums[i] == 0:
                    nums[i] = -1 * (n + 1)
        print(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i
        return n + 1
            