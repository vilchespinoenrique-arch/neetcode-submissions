class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row = len(grid)

        col = len(grid[0]) 


        number_of_island = 0





        def recursion(r,c):   # here we want the 4 ways og movement. they will move on way the most they can and then tried the other side 

            
            # we need the boundary checks 

            # if we either go out of bounds, or we encounter a 0, go ahead and retur 

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
                return 

            # make the number we just use a 0 


            grid[r][c] = "0"
             
            
            
            recursion(r, c + 1) # right side 

            recursion(r + 1, c) # down 

            recursion(r, c - 1) # left 

            recursion(r - 1, c) # up

        
        
        
        for r in range(row):
            for c in range(col): 
                
                if grid[r][c] == "1":
                    number_of_island += 1
                    recursion(r,c)

        return number_of_island






