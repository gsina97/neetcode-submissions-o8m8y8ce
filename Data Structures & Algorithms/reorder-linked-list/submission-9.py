# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer.
        # break lingage on two lists.
        # reverse second list.
        # append 
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp


        
        first = head
        second = prev

        while first and second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        
        