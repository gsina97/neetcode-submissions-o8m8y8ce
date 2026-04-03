class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        median1 = median2 = 0

        l1 = len(nums1)
        l2 = len(nums2)
        i = j = 0
        for _ in range((l1 + l2) // 2  + 1):
            median2 = median1
            if i < l1 and j < l2:
                if nums1[i]  > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < l1:
                median1 = nums1[i]
                i += 1
            elif j < l2:
                median1 = nums2[j]
                j += 1
            
        if (l1 + l2) % 2 == 0:
            return (median1 + median2) / 2
        else:
            return median1