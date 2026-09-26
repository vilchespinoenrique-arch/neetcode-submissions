# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # inorder traersal is left root first, then the parent, and then the right one 

        res = []

        def recursion(node): 

            if not node:
                return
        
        
            recursion(node.left)
            res.append(node.val)
            recursion(node.right)
    
        recursion(root)
        return res 

            
        