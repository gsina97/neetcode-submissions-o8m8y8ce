class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m1 = m2 = 0

        l1 = len(nums1)
        l2 = len(nums2)

        p1 = p2= 0
        for i in range((l1 + l2) // 2 + 1):
            m2 = m1
            
            if p1 < l1 and p2 < l2:
                if nums1[p1] < nums2[p2]:
                    m1 = nums1[p1]
                    p1 += 1
                else:
                    m1 = nums2[p2]
                    p2 += 1
            elif p1 < l1:
                m1 = nums1[p1]
                p1 += 1
            else:
                m1 = nums2[p2]
                p2 += 1
        
        print(m1, m2)
        if (l1 + l2) % 2 == 0:
            return (m1 + m2) / 2
        else:
            return m1