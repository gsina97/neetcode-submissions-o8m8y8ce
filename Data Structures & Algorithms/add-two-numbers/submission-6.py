# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0,None)
        dummy = ListNode(0, curr)
        
        carry = 0
        while l1 and l2:
            
            res = l1.val + l2.val + carry
            if res > 9:
                carry = res // 10
            else:
                carry = 0
            res = res % 10
            node = ListNode(res)
            curr.next = node
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            res = l1.val + carry
            if res > 9:
                carry = res // 10
            else:
                carry = 0
            res = res % 10
            node = ListNode(res)
            curr.next = node
            curr = curr.next
            l1 = l1.next
        while l2:
            res = l2.val + carry
            if res > 9:
                carry = res // 10
            else:
                carry = 0
            res = res % 10
            node = ListNode(res)
            curr.next = node
            curr = curr.next
            l2 = l2.next

        
        if carry:
            node = ListNode(carry)
            curr.next = node
            curr = curr.next
        
        return dummy.next.next
