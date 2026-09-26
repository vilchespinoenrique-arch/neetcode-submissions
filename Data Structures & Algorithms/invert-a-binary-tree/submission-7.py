# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        # notice that they want me to return the root of the binary tree. 

        # so im not trying to get the output that is there, the only thing im doing is inverting the tree. and this can be achieved by inverting the nodes one by one, but we want to invert the bottom of the leaf first, and then go up from there using recursion 


        if root == None: 

            return 

        
        left = self.invertTree(root.left)

        # right here we would go all the way down to the left, till we get hit with root being none, and then we would return and go to the next line 
        right = self.invertTree(root.right)

        # here becasuse we return to the 4, we would go to the right side of the the tree wchih also happens to be none 

        # so right now: 

        # right = none 

        # left = none 

        # now we want to invert that 



        root.left = right 

        root.right = left 


        # so here we jsut switch them 


        return root 

