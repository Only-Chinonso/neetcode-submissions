# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [[root,1]]
        while stack:
            node,deap = stack.pop()
            if node:
                append([node.right,deap+1])
                append([node.left,deap+1])
                res = max(m,deap)
        return res
