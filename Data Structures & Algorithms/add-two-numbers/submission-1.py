# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        place_val = 1
        l1_val = 0
        l2_val = 0
        while l1 and l2:
            l1_val += (l1.val * place_val)
            l2_val += (l2.val * place_val)
            place_val *= 10
            l1, l2 = l1.next, l2.next
        
        if l1:
            while l1:
                l1_val += (l1.val * place_val)
                place_val *= 10
                l1 = l1.next
        elif l2:
             while l2:
                l2_val += (l2.val * place_val)
                place_val *= 10
                l2 = l2.next
        
        total = l1_val + l2_val
        dummy = res = ListNode()

        if total == 0:
            return ListNode(0)
        while total > 0:
            digit = total % 10
            res.next = ListNode(digit)
            res = res.next
            total = total // 10
        
        return dummy.next


           
        



        
