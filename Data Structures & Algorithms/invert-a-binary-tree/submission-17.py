# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # in order to invert a tree, we would set left side as left, and run through left, 

        # and then do the same thing with the right side, and then do 

        # left, right = root.right, rooot.left 

        def invert(node):

            if node == None: 

                return 


            left = invert(node.left) 


            right = invert(node.right) 


            node.left = right 

            node.right = left 

            return node 

        invert(root)

        return root 

      