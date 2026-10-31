class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:
            c = left + (right - left) // 2
            if nums[c] == target:
                return c
            elif nums[c] > target:
                right = c - 1
            else:
                left = c + 1
        return -1