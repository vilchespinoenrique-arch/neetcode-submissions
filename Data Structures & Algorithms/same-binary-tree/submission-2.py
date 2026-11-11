# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        # for this question we are going to grab p and we are going to grab q and we are going iterate throught both using recurison and we are going to compare each other 


        if p == None and q == None: # if both are none, then we can go ahead and return true right away 
            
            return True 

        if p == None or q == None: # if only one of them is a none, go ahead and return fasle, becasue they have to be equal 

            return False 



        if p.val != q.val: 

            return False 

        
        else: 

            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

        