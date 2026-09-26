class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        

        triangle = [] 

        


        for number in range(numRows): 


            row = [1] * (number + 1) # this will make sure that we get the rows, that we want, so it will look like this: 

            
            # row = [1]

            # then row = [1,1] 

            # row = [1,1,1] and so on and on 



            for i in range(1, number): # we will set a for loop that will be in charge of the main math that needs to happenn between rows. 

                row[i] = triangle[number - 1][i -1] + triangle[number - 1][i] 


            triangle.append(row)

        return triangle