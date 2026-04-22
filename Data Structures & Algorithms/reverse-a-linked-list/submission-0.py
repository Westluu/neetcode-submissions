# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3
        if not head:
            return None
        cur = head.next
        result = ListNode(head.val, None)
        while cur != None:
            result = ListNode(cur.val, result)
            cur = cur.next
        return result

        