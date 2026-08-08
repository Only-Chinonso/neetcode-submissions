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
        copy = head
        Copy = Node(0)
        hashmap = {}
        while copy:
            hashmap[copy] = copy.random
            copy = copy.next
        prevr = None
        for ran in hashmap.values():
            nxt = Copy.next
            Copy.next = head
            Copy.random
            Copy = nxt
            head = head.next
            prevr = ran
        return Copy.next

            