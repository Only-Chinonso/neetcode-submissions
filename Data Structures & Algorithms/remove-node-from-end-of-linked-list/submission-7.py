# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head = res= prev
        for _ in range(n - 1):
            head = head.next
        if head.next:
            head.next = head.next.next
        else:
            head.next = None
        prev = None
        while res:
            nxt = res.next
            res.next = prev
            prev = res
            res = nxt
        return prev
            
