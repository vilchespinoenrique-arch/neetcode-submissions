# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


            def check_leaves(node, leaves):


                if node == None: 

                    return 

                
                if node.left == None  and node.right == None:  # means that they are a leaf, so they dont have any childs 

                    leaves.append(node.val)
                    return 

                
                check_leaves(node.left, leaves)


                check_leaves(node.right, leaves)


            

            leaves1 = []

            check_leaves(root1, leaves1)



            leaves2 = []

            check_leaves(root2, leaves2)


            return leaves1 == leaves2 

            # it will return whatever they have there 





