# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        len_vals = 0
        vals = list()

        curr = head
        while curr:
            vals.append(curr.val)
            len_vals += 1
            curr = curr.next

        max_twin = 0
        for i in range(len_vals // 2):
            twin_val = (vals[i] + vals[-1 - i])
            max_twin = max(max_twin, twin_val)

        return max_twin