class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        r = 0
        count = 0

        for num in nums:
            if count == 0:
                r = num
            if r == num: count += 1
            else: count -= 1
    
        return r
