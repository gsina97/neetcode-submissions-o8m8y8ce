class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxi = 0

        for n in hashSet:
            if n - 1 not in hashSet:
                length = 0
                while (n + length) in hashSet:
                    length += 1
                maxi = max(length, maxi)
        return maxi