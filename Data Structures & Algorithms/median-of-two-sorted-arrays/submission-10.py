class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i , j = 0,0
        len1 = len(nums1)
        len2 = len(nums2)
        totalLen = len1 + len2
        median1 = median2 = 0

        for idx in range(totalLen // 2 + 1):
            median2 = median1

            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            elif j < len2:
                median1 = nums2[j]
                j += 1
        
        if totalLen % 2 == 0:
            print("here")
            print(median1)
            print(median2)
            return (median1+median2) / 2
        else:
            return median1
