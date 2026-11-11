class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass


        # for this question we want to set a mid, and then do the same idea that we would do with a binary search 


        def check(low, high): 
            
            if low > high: 
                
                return None 
            
            m = (low + high) // 2 

        

            root = TreeNode(nums[m])


            root.left = check(low, m - 1)


            root.right = check(m + 1, high)


            return root 

        
        return check(0, len(nums)- 1)


        # nums  = [ 3,  7,  9, 12, 15, 20, 25 ]
        # index:    0   1   2   3   4   5   6


        # low = 0  -> 3 

        # high = 6  -> 25 

        # m = 3 -> 12 

        # root = 12 

        # root.left = check(0, 2)

        # now we do the root.left 

        #  low = 0 -> 3 

        # high = 2 -> 9 


        # mid = 1 -> 7 

        # root = 7 

        # root.left = check(0, 0)


        # check(0 0) 

        # low = 0 -> 3 

        # high = 0 -> 3

        # mid = 0 -> 3 

        # root = 3 

        # root.left = 3 

        # then we hit a limit so it return none, after we get that none, 

        # so we go back to check(0, 0), and we will have low be bigger so we will have none, 

        # so the 3 will have none to to thje right and the left, and now we go back 


        #  root.right = check(0, 2)

        # low = 2 -> 

        # high = 2 -> 9 

        # root = 9 

        # then root.right would be that 9, and this will have none for the left and right side


        # then we go back 

        # 
        # low = 0  -> 3 

        # high = 6  -> 25 

        # m = 3 -> 12 

        # root = 12 

        # and we do this with the right side 

        # low = 4 -> 15

        # high = 6 -> 20 

        # mid = 5 -> 25 
