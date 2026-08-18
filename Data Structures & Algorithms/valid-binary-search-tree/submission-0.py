# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True

            left,right = node.left,node.right 

            if left:
                if left.val < node.val:
                    return dfs(left)
                return False

            if right :
                if left.val > node.val:
                    return dfs(right)
                return False
        return dfs(root)