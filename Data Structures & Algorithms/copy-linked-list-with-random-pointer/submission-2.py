"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_idx_map = dict()
        idx_dc_map = dict()

        if not head:
            return head

        dc_head = Node(head.val, random = head.random)
        dc_prev = dc_head

        original_idx_map[head] = 0
        idx_dc_map[0] = dc_head 

        curr = head.next
        idx = 1
        while curr:
            dc = Node(curr.val, random = curr.random)
            dc_prev.next = dc
            dc_prev = dc
 
            original_idx_map[curr] = idx
            idx_dc_map[idx] = dc

            curr = curr.next
            idx += 1

        curr = dc_head
        while curr:
            if curr.random: 
                curr.random = idx_dc_map[original_idx_map[curr.random]]
            curr = curr.next

        return dc_head


        