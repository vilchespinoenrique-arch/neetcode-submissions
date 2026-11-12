# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        # there is another way to do this and is to use the fact the is a binary search tree, so we can do something else 


        total = 0 



        def check(node): 
            
            nonlocal total 

            if node == None: 


                return 

            if low <= node.val <= high: 

                total += node.val 


            check(node.left)


            check(node.right)

        check(root) 

        return total 

            


            