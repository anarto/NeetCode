class Solution:
    def search(self, nums: List[int], target: int) -> int:


        n = len(nums)
        left, right = 0, n - 1

        while left <= right:

            center = left + (right - left) // 2

            if nums[center] == target:
                return center

            # left sorted portion
            if nums[left] <= nums[center]:
                if nums[left] > target:
                    left = center + 1
                elif nums[center] < target:
                    left = center + 1
                else:
                    right = center - 1
            # right sorted portion
            else:
                if nums[right] < target:
                    right = center - 1
                elif nums[center] > target:
                    right = center - 1
                else:
                    left = center + 1

        return -1

        