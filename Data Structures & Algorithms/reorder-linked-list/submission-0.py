# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, fast = head, head.next
        
        #get middle of list
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        #reverse the list from mid
        second = mid.next
        mid.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev
        while second:
            f_nxt = first.next
            s_nxt = second.next
            first.next = second
            second.next = f_nxt
            first = f_nxt
            second = s_nxt
        
        return 
        


        