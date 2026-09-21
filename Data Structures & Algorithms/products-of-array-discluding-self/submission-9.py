class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pre = 1
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            prefix[i] = pre
            pre = pre * nums[i]
        
        pos = 1
        postfix = [0] * len(nums)
        for i in range(len(nums) -1 , -1 , -1):
            postfix[i] = pos
            pos = pos * nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(postfix[i] * prefix[i])
        
        return res