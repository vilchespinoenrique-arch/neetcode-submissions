class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # for the island perimeter we want add + 1 everytime we get out of bound, becasue that means we can add 1 

        # and we will return a 0. if we have already been there in a visisted 



        row = len(grid)

        col = len(grid[0])

        visited = set()


        def all_direction(r,c): # r and c representing the row and the collumn of the grid 

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0: 

                return 1 

                # if we go out of bounds or we see water go ahead and return 1 

            if (r,c) in visited:
                return 0 # now that we have gone through this you can go ahead and added to visited 

            
            # if we hit another 1, you can go ahead and return 0, becasue we dont want to add anything more to it 
            visited.add((r,c)) 

            perimeter = 0 
            
            perimeter += all_direction(r, c + 1) # right 

            perimeter += all_direction(r - 1, c) # up 

            perimeter += all_direction(r, c - 1) # left 

            perimeter += all_direction(r + 1, c) # down 

            return perimeter 


        # lets run this example: 

        # we start in 0,0. then we go to the right and thenw go tot he right again and we return with 1 

        # so perimeter = 0 + 1 

        # then perimeter = 1 + 1

        # then perimeter = 2 + 0 

        # then perimeter = 2 + 1 

        # so now perimeter 3. but we finish so we return perimeter. and with that 3 perimeter, we go back

        # and then the last call will  hold that 3 perimeter value, right and that return perimeter is returining for that 


        for r in range(row):
            for c in range(col):
                
                if grid[r][c] == 1: 

                    return all_direction(r,c)

        return 0