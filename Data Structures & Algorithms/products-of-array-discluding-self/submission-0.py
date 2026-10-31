class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix_products = [1] * n
        for i in range(n):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1] if i > 0 else 1

        suffix_products = [1] * n
        for i in range(n - 1, -1, -1):
            suffix_products[i] = nums[i + 1] * suffix_products[i + 1] if i < n - 1 else 1

        return [prefix_products[i] * suffix_products[i] for i in range(n)]
