# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            s = val1+ val2 + carry
            carry = 0
            if s > 9:
                carry = s // 10
            newVal = s % 10
            node = ListNode(newVal)
            curr.next = node
            curr = curr.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return dummy.next