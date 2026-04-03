class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for item in nums:
            count[item] = count.get(item, 0) + 1

        for value, frequency in count.items():
            freq[frequency].append(value)

        res = []
        for i in range(len(freq) -1 , 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res