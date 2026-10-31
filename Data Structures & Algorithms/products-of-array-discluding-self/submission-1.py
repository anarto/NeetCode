class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        products = [1] * n

        p = 1
        for i in range(n):
            products[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(n - 1, -1, -1):
            products[i] *= p
            p *= nums[i]

        return products