# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # root-left-right
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # stack = []
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        # return res

        res = []
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   5
            
