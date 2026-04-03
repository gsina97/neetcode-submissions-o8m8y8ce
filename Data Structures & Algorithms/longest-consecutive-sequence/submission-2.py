class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) # contains letts:
        total = 0

        for num in nums:
            if num - 1 in s:
                continue
            curr = 1
            while num + 1 in s:
                num += 1
                curr += 1
            total = max(total, curr)
        return total

