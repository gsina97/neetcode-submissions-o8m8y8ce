class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        s = []

        def p():
            if len(s) == len(nums):
                res.append(s[:])
                return

            for n in nums:
                if n not in s:
                    s.append(n)
                    p()
                    s.pop()

        p()
        return res
