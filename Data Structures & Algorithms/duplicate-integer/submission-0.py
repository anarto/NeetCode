class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_so_far = set()
        for num in nums:
            if num in seen_so_far:
                return True
            seen_so_far.add(num)
        return False