# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0, True
            lh, lb = height(node.left)
            rh, rb = height(node.right)
            balanced = True if ((abs(lh - rh) <= 1) and lb and rb) else False
            return (1+max(lh,rh)), balanced
        h, b = height(root)
        return b