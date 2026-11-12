# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        


        def check(node, current): 


            if node == None:

                return False 


            current += node.val 


            if node.left == None and node.right == None: 

                return current == targetSum 


            
            return check(node.left, current) or check(node.right, current) 


        return check(root, 0)