class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        out = 0

        for n in s:
            if n - 1 not in s:

                longest = 0
                while longest + n in s:
                    longest += 1
                out = max(out, longest)
        return out