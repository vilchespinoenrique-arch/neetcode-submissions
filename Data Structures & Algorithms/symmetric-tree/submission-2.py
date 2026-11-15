# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        



        def check(a, b): 


            if a == None and b == None: 

                return True 

            
            if not a or not b: 


                return False # if only one of them is not right then we will go ahead and return fasle 


            if a.val != b.val: 

                return False 

            
            return check(a.left, b.right) and check(a.right, b.left)

        

        return check(root.left, root.right)