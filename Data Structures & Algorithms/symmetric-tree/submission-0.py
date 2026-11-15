# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        # okay so what we want to do for this question is we want to have a and b

        # the reason we want that is becasue we want them to be compared to each other at the same time 


        def check(a,b): 


            if a == None and b == None: 

                return True # if both are none, then we return true becasue it they both are missing 

            
            if not a or not b: # if one of them is there and the other one isnt then return fals e

                return False 


            if a.val != b.val: 

                return False 

            
            return check(a.left, b.right) and check(a.right, b.left) # we have to check the left side with the right side and also the right side with the left side. both of them 
        
        return check(root.left, root.right)
        