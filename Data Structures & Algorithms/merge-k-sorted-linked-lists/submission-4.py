# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def merge2List(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                curr = curr.next
            
            if l1:
                curr.next= l1
            if l2:
                curr.next = l2
            
            return dummy.next

        while len(lists) != 1:
            l = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp = merge2List(l1, l2)
                l.append(temp)
            lists = l
        return lists[0]


        



    