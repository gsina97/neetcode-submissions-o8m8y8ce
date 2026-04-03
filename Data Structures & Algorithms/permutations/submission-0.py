class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # Base case: if we've fixed every position, add the current state
            if start == len(nums):
                res.append(nums[:]) # nums[:] creates a copy
                return

            for i in range(start, len(nums)):
                # 1. Swap: Put the element at index 'i' into the 'start' position
                nums[start], nums[i] = nums[i], nums[start]

                # 2. Recurse: Move to the next position
                backtrack(start + 1)

                # 3. Backtrack: Swap back to restore the original state for the next loop
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res