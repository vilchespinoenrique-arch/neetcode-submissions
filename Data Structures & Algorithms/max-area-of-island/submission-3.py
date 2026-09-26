class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        row = len(grid) 

        col = len(grid[0])


        best = 0 


        def recursion(r , c):

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                
                return 0

            grid[r][c] = 0 # make sure you turn the current one, because otherwise we will see repeated values 

            area = 1

            area += recursion(r, c + 1)


            area += recursion (r + 1, c) 

            area += recursion (r, c - 1) 

            area += recursion (r - 1, c) 


            return area 

        for r in range(row):
            for c in range(col): 

                if grid[r][c] == 1:

                    best = max(best, recursion(r,c))

        
        return best 
        
