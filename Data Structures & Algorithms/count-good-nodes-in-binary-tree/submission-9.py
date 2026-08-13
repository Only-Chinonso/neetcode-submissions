# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append(root)
        res = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    left = node.left.val if node.left else -200
                    right = node.right.val if node.right else -200
                    if left >= node.val:
                        res += 1
                    if right >= node.val:
                        res += 1

                    q.append(node.left)
                    q.append(node.right)
        return res

