# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        maxh = 0
        while stack:
            curr, h = stack.pop()
            if not curr:
                continue
            maxh = max(maxh, h)
            if curr.left:
                stack.append((curr.left, 1+h))
            if curr.right:
                stack.append((curr.right, 1+h))
        return maxh
        
        # if not root:
        #     return 0
        # rightDepth = self.maxDepth(root.right)
        # leftDepth = self.maxDepth(root.left)
        # height = 1 + max(rightDepth, leftDepth)

        # return height
        