class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        subset = []

        def depth_first_search(level):
            if level >= len(nums):
                subsets.append(subset.copy())
                return

            # to include nums[i]
            subset.append(nums[level])
            depth_first_search(level + 1)


            #  We've run the function with nums[level], now we need to run the function without it.

            # NOT to include nums[i]
            subset.pop()
            depth_first_search(level + 1)

        depth_first_search(0)
        return subsets