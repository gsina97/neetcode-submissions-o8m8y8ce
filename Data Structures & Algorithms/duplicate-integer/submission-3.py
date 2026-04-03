class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}
        for i in nums:
            if i in store:
                return True
            store[i] = True
        
        return False