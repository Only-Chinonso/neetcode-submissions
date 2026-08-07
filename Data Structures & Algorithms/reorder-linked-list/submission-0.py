# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second 
            second = nxt
        first,second = head,prev
        while second:
            fo = first.next
            so = socond.next
            first.next = second
            second = fo
            second = so
            first = fo
        