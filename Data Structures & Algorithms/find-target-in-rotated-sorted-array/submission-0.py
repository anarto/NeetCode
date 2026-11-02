class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        left, right = 0, n - 1

        while left <= right:

            c = left + (right - left) // 2

            if nums[c] == target:
                return c
            
            if nums[left] <= nums[c]:
                if nums[c] < target or nums[left] > target:
                    left = c + 1
                else:
                    right = c - 1
            else:
                if nums[c] > target or nums[right] < target:
                    right = c - 1
                else:
                    left = c + 1
        return -1