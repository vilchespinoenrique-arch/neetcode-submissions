# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # this is we go left, 

        res = [] 

        def tree(node):

            if not node:
                return 

            tree(node.left)

            tree(node.right)

            res.append(node.val)

        tree(root)
        return res 

        