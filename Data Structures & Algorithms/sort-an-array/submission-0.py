# Sort an Array

# You are given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
# Example 1:
# Input: nums = [10,9,1,1,1,2,3,1]

# Output: [1,1,1,1,2,3,9,10]
# Example 2:
# Input: nums = [5,10,2,1,3]

# Output: [1,2,3,5,10]
# Constraints:
# 1 <= nums.length <= 50,000.
# -50,000 <= nums[i] <= 50,000


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, nums: list[int], left: int, right: int):
        if left < right:
            center = left + (right - left) // 2
            self.mergeSort(nums, left, center)
            self.mergeSort(nums, center + 1, right)
            self.merge(nums, left, center, right)

    def merge(self, nums: list[int], left: int, center: int, right: int):

        numsL = nums[left : center + 1]
        numsR = nums[center + 1 : right + 1]

        n1 = len(numsL)
        n2 = len(numsR)

        p, q, r = 0, 0, left

        while p < n1 and q < n2:
            if numsL[p] <= numsR[q]:
                nums[r] = numsL[p]
                p += 1
            else:
                nums[r] = numsR[q]
                q += 1
            r += 1

        while p < n1:
            nums[r] = numsL[p]
            p += 1
            r += 1

        while q < n2:
            nums[r] = numsR[q]
            q += 1
            r += 1


# assert Solution().sortArray([10, 9, 1, 1, 1, 2, 3, 1]) == [1, 1, 1, 1, 2, 3, 9, 10]
# assert Solution().sortArray([5, 10, 2, 1, 3]) == [1, 2, 3, 5, 10]
