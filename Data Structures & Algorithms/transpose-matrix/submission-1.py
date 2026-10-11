class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # for this question we are going to transpose the matrix, and this is honestly something i should know how to do, but sadly i dont. the thing is that the way you do this is pretty standard 


        # so we are going to be swithcing the rows with the columns and the columns with the rows 


        rows = len(matrix)

        columns = len(matrix[0])



        # now we know that the result will be the columns, will be the amount of rows 


        # lets use this example Input: [
#                        [1,0,5],
 #                       [2,4,3]


                 
#                        [1,2],
 #                       [0,4],
  #                      [5,3]

# this is actually equivalent to -> [0, 0], [0,0], [0,0]

# just so that you dont get confused by it 

        result = []

        for _ in range(columns):

            row = []

            for _ in range(rows):

                row.append(0)

            result.append(row)



        # now are result is correctly holding the 0

        # now lets go 1 by 1 


        for r in range(0, rows): 

            for c in range(0, columns): 


                # now that we are going 1 by 1 


                result[c][r] = matrix[r][c]

        return result 

