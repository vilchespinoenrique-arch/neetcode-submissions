# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # for this question is important to understand the difference between 2 thigns 

        # the diamter and the height.

        # the dimater is the add ones from you left and right side. however you can only use the same node once, unless is the parent. 

        # for example the diamter on that first example cannot be 1 → 2 → 3 → 5 + 1 → 2 → 4 → 6 and the reason for this is becasue that number 2 repeats itself, so is not allowed 


        # now in order to get the diamter we have to set the global variable to 0, and then we add the left and the right side 

        
        diameter = 0 

        def height(node): 
            nonlocal diameter 

            if node == None: 

                return 0 

            
            left = height(node.left)

            right = height(node.right) 


            diameter = max(diameter, right + left) 

            return max(left,right) + 1 # get the height so that we can move around


        height(root)

        return diameter # but how can we get the last call of diameteR? 



        # i want to run into what is happenign exactly so that we have an idea of what is going on 


        # root = 1 -> left  = 2 , -> left = 3, -> left = 5 

        # now left will keep going and it will return 0, so left = 0 

        # right will do the same thing and it will return 0 

        # so diamter = 0 

        # and it will retunr 1 for the heigt. 


        # now we move back to the 3 , and we move to the right whcih is 0 

        # so now we have left = 1 and right = 0 

        # so the diamter = 1 

        # and the height will be 2 


        # now we go back to the 2, and in the left side we have = 2, and on the right side becasue of the same method we will have 1 

        # so the diameter will be 2 + 1 = 3 it will give 3 

        # diameter = 3 



        # now if we go back to that first node, we have left side = 0, and right side = 3 

        # if we add them together we get 3 as well. so 3 is the max diameter! 

        