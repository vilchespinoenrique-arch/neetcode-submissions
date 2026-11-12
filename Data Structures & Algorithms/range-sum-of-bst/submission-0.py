# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        

        total = 0 


        def check(node): 

            nonlocal total 


            if node is None:
                return 

            if low <= node.val <= high: 

            # val = 2  - > 3 < 2 > 8   -> wrong
 
            # val = 5 ->  3 < 5 < 8    -> correct 
  
                total += node.val 

            
            check(node.left)

            check(node.right)

        check(root)

        return total  