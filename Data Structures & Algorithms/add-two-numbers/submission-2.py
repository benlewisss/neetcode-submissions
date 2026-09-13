# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Completed WITHOUT HELP in 45 minutes (+ probs like 5-10 mins ish kind of pondering elsewhere.)
# Only help I got was to extract digit from a number using // and % but in hindsight that's obvious.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        curr2 = l2

        carry_over = 0

        while curr1:
            curr2_placeholder = 0
            if curr2:
                curr2_placeholder = curr2.val

            new_val = curr1.val + curr2_placeholder + carry_over
        
            # Extract the smallest digit
            curr1.val = new_val % 10
            # The rest carries over
            carry_over = new_val // 10

            if curr2 and curr2.next:
                curr2 = curr2.next
            else:
                curr2 = None

            if curr1 and curr1.next:
                curr1 = curr1.next
            else:
                break

        while curr2:
            new_val = curr2.val + carry_over
            # Extract the smallest digit
            curr1.next = ListNode(new_val % 10)
            # The rest carries over
            carry_over = new_val // 10

            curr1 = curr1.next
            curr2 = curr2.next
            
        if carry_over > 0:
            curr1.next = ListNode(carry_over)

        return l1



