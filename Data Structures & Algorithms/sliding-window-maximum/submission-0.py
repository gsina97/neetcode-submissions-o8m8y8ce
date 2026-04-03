class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        res = []

        for r in range(len(nums)):

            # 1. Remove smaller values from the back
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            # 2. Add current index
            dq.append(r)

            # 3. Remove elements outside the window ()
            if dq[0] < r - k + 1:
                dq.popleft()

            # 4. Record max once window size is k
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res
