# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1 - find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2 - reverse second half
        second = slow.next
        slow.next = None          # cut list in half
        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev             # prev is new head of reversed half

        # step 3 - merge alternating
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
        
        