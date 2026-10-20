# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        

        if left == right:
            return head

        node_number = 0

        left_prev = None
        left_node = None

        right_node = None
        right_next = None
    
        prev = None
        curr = head
        while curr:
            node_number += 1   

            tmp_next = curr.next

            if (node_number >= left) and (node_number <= right):
                if (node_number == left):
                    left_prev = prev
                    left_node = curr

                elif (node_number == right):
                    right_node = curr

                curr.next = prev

            if (node_number == right + 1):
                right_next = curr

            prev = curr
            curr = tmp_next

        left_node.next = right_next
        if left_prev: 
            left_prev.next = right_node

        if left_prev:
            return head
        else:
            return right_node
        

        
