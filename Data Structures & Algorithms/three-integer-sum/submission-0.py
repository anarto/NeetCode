class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()

        answer = []
        
        i = 0
        while i < n:
            a = nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                tSum = a + b + c
                if tSum == 0:
                    answer.append([a, b, c])
                    while left < right and nums[left] == b:
                        left += 1
                    while left < right and nums[right] == c:
                        right -= 1
                elif tSum > 0:
                    right -= 1
                else:
                    left += 1
            while i < n and nums[i] == a:
                i += 1
        return answer
                