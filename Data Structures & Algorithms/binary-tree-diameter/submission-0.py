# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            lh = depth(root.left)
            rh = depth(root.right)
            res = max(res, lh+rh)
            return 1 + max(lh,rh)
        depth(root)

        return res
            