# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # A 1 2 4
        # B 1 3 5
        # R 1 -> 1 -> 2 -> 3 -> 4 -> 5

        #A 1 2 2 3
        #B 1 3 5
        #R 1 -> 1 -> 2 -> 2 -> 3 -> 3-> 5

        #solution
        #1. for the 1st element check A and B and start off if the smallest value and increment that list
        #2. add that value into the result
        #3. compare the rest of the list using 1. until all elements are done

        #running time o(n + m)

        sorted_list = ListNode()
        result = sorted_list
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        if list1:
            result.next = list1
        elif list2:
            result.next = list2
        return sorted_list.next
