class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0,0
        s1Len = len(nums1)
        s2Len = len(nums2)
        totalLen = s1Len + s2Len


        median1 = median2 = 0
        for idx in range(totalLen // 2 + 1):

            median2 = median1

            if i < s1Len and j < s2Len:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j +=1
                else:
                    median1 = nums1[i]
                    i += 1
            elif i < s1Len:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
        
        if totalLen % 2 == 0:
            return (median1 + median2) / 2
        else:
            return median1