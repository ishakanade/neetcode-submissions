# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack1 = [root]
        stack2 = []
        while stack1:
            curr = stack1.pop()
            stack2.append(curr)

            if(curr.left):
                stack1.append(curr.left)
            if(curr.right):
                stack1.append(curr.right)
        while stack2:
            res.append(stack2.pop().val)
        return res
        # res = []
        # def postorder(root):
        #     if not root:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     res.append(root.val)
        # postorder(root)
        # return res