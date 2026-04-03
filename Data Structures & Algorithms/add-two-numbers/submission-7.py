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
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            res = v1 + v2 + carry
            if res > 9:
                carry = res // 10
            else:
                carry = 0
            res = res % 10
            node = ListNode(res)
            curr.next = node
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # if carry:
        #     node = ListNode(carry)
        #     curr.next = node
        #     curr = curr.next
        
        return dummy.next.next
