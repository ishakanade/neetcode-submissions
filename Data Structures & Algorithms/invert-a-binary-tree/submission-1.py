# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                stack.append(curr.left)
                stack.append(curr.right)
        return root
        
        # curr = root
        # # root right left go right repeat come to left repeat
        # if not root:
        #     return None
        # curr.left, curr.right = curr.right, curr.left

        # self.invertTree(curr.left)
        # self.invertTree(curr.right)
        # return root