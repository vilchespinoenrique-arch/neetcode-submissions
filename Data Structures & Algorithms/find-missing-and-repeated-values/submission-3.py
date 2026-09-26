class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        hashmap = {} 

        result = []



        for row in grid: 

            for column in row: 

                hashmap[column] = hashmap.get(column, 0) + 1



        # now we will have each element in our hashmap with their values 


        # { 1: 1, 3: 1, 2: 2} 


        for key in hashmap.keys(): 

            if hashmap[key] == 2: 

                result.append(key) # this will append the value of the key we put, which has a value of 2 

        


        for i in range(1, len(grid) * len(grid[0]) + 1):


            if hashmap.get(i, 0) == 0:

                result.append(i)
                
        return result 
        
        

