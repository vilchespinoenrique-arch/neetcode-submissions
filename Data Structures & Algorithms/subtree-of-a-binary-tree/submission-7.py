# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        # for this quesiton we want to first have a function that can compare nodes, we will use this and we will pass it throught the different parts, then we are going to keep going until we find a True or a False, but it will be going for a while, you will see 


        def check(root, subRoot): 

            if not root and not subRoot: 

                return True 


            if not root or not subRoot:

                return False 

            
            if root.val != subRoot.val: 

                return False 


            
            else: 
                
                return check(root.left, subRoot.left) and check(root.right, subRoot.right) # only if both are true you would retunr true, if even one of them is false, you will return false

        
        if not root:

            return False 

        if not subRoot:

            return True 

            

        if check(root, subRoot): 

            return True 


        else:  


            return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right, subRoot) 
