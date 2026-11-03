class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        left, right = 0, n - 1

        minimum_so_far = nums[0]

        while left <= right:

            if nums[left] < nums[right]:
                return min(nums[left], minimum_so_far)

            center = left + (right - left) // 2
            minimum_so_far =  min(nums[center], minimum_so_far)
            if nums[left] <= nums[center]:
                left = center + 1
            else:
                right = center - 1
        
        return minimum_so_far