# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        res = int(num1) + int(num2)
        res = str(res)
        head = ListNode(res[0])
        for i in range(res):
            node = ListNode(n)
            if i != len(res) - 1:
                node.next = res[i + 1]
            else:
                node.next = None
        return head