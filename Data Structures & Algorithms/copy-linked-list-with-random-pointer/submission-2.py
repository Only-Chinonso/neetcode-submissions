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
        Copy = Node(0,0,0)
        hashmap = {}
        while copy:
            hashmap[copy] = copy.random
            copy = copy.next
        r = None
        n = head 
        for ran in hashmap.values():
            Copy.next = n
            Copy.random = r
            Copy = Copy.next
            n = n.next
            r = ran
        return Copy.next

            