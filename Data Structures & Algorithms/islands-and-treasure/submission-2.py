from collections import deque 

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        row = len(grid)

        col = len(grid[0])
        
        queue = deque()


        inf = 2147483647 



        for r in range(row):

            for c in range(col): 

                if grid[r][c] == 0:

                    queue.append((r,c))


        while queue: 

            r, c = queue.popleft()


            directions = [

                (1,0), # up
                (0,1),  # right 
                (-1, 0), # down
                (0, -1) # left 
                
                ]



            for rm, cm, in directions:

                current_row = rm + r 


                current_col = cm + c 

                # this will update both of my currection direction, to go up, right, down, and left 


                if 0 <= current_row < row and 0 <= current_col < col and grid[current_row][current_col] == inf: 

                    grid[current_row][current_col] = grid[r][c] + 1 # so the grid that we come from, should have a value, it could be 0, or it could be 1, meaning that it was a numebr we changed before 

                    queue.append((current_row, current_col))