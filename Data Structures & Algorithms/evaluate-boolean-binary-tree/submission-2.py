# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:


        # for this question we want to treat: 

         # 0 -> False 

         # 1 -> True 


         # 2 -> or 


         # 3 -> and 


         # knowing this we can do this 



        if not root.left and not root.right: # meaning that this is a leaf

            if root.val == 1: 

                return True 

            elif root.val == 0: 

                return False 


        
        if root.val == 2:

           return (self.evaluateTree(root.left) or self.evaluateTree(root.right) )



        if root.val == 3: 

            return (self.evaluateTree(root.left) and self.evaluateTree(root.right)) 


    # lets run an example to see if this works 



    # first node is 3, so we will go to the left side first 


    # 3 -> 1      1 is true so that will be true, so for the and the left side will return true 


    # now we go back to the and, and we move on to the right side which is 


    # 2 -> 2 now has a and, so we go to the left then the right, for the left side we have false and then for the right side we have true, and that will return true. 


    # now we have left side being true and left side being true so that will return true 




        