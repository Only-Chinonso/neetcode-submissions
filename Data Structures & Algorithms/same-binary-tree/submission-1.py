# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p != q:return False
        def dfs(b1,b2):
            if not b1 or not b2:
                return True
            elif b1.left == b2.left and b1.right == b2.right:
                return True if dfs(b1.left,b2.left) and dfs(b1.right,b2.right) else False
            else:
                return False
        return dfs(p,q)
            
            