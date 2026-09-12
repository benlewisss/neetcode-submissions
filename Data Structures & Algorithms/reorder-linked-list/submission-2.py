# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# COMPLETED ON MY OWN IN 26 MINUTES
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # After reading and understanding question, the actions taken can be generalised 
        #in the formula [0, n-1, 1, n-2, 2, n-3, ...] from nodes 0 to n-1. 
        # So, essentially what this is:
        # - Split the linked list into two halfs (the second half being shorter if length is odd)
        # - Reverse the second half
        # - Insert it after every node in the first half. Bam. Done.

        # Edge cases
        if not head.next:
            return

        # Step 1: Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = ListNode(slow.next.val, slow.next.next)
        slow.next = None

        # Step 2: Reverse second half

        prev = None
        curr = second_half
        while curr:
            tmp = ListNode(curr.val, curr.next)
            curr.next = prev
            prev = curr
            curr = tmp.next

        reversed_second_half = prev
        
        # Step 3: Combine

        curr1 = head
        curr2 = reversed_second_half
        while curr2 and curr1:
            tmp1_next = curr1.next
            tmp2_next = curr2.next

            curr1.next = curr2
            curr2.next = tmp1_next

            curr1 = tmp1_next
            curr2 = tmp2_next
        
 

