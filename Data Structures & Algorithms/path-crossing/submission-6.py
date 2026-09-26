class Solution:
    def isPathCrossing(self, path: str) -> bool:

        # for this question we want to use tupples and included them in a set. 

        # so everytime a pair is seen we are going to put it in the set, 

        # and if for some reason the value was is seen before then we will return True, becasue it would mean the value is repeating 


        seen = set() 

        origin = (0,0)

        seen.add(origin)

        x,y = origin 


        for i in range(len(path)): 

            

            if path[i] == 'N':  # up

                y = y + 1 

                origin = (x, y)

                if origin in seen: 

                    return True 

                else:               

                    seen.add(origin)
        


            if path[i] == 'W': # left

                x = x -1 

                origin = (x,y)

                if origin in seen: 

                    return True 

                else:               

                    seen.add(origin)

            if path[i] == 'S': # down 

                y = y - 1

                origin = (x, y)

                if origin in seen: 

                    return True 

                else:               

                    seen.add(origin)
            
            if path[i] == 'E': # right 
                
                x = x + 1                

                origin = (x,y)

                if origin in seen: 

                    return True 

                else:               

                    seen.add(origin)

                

            

        return False
        