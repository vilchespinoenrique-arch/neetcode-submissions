# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # this question has a simple idea we want to go through the left node and the right node of using recurison of the tree
        if not root:
            return None

        # if there is not root then return -1 

        left = self.invertTree(root.left) 
        right = self.invertTree(root.right)

        root.left, root.right = right, left 

        return root 



        