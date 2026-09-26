class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        result = []
        

        for number in range(rowIndex + 1): 


            rows = [1] * (number + 1)    # this would be equal to 

            #  rows =[1] * 0 + 1 = 1  rows[1] * 1 = 


            
            # okay so doing them all at once is not a good idea.


            # right now we have row = [1]

            # right now we are at row = [1,1]

            # right no we are at row = [1,1,1]

            # right now we have row = [1,1,1,1]


            for i in range(1, number): # we do not want to further thant that 

                # this will only start once we have number =2 , and so that is perfect, becasue when number is 2

                # we will have [1, 1, 1] and we can finally do something 



                rows[i] = result[number - 1][i - 1] + result[number - 1][i]

                # this will make rows[1]  from the row that we are on 

                # which is row = [1, 1, 1]
 
                # so row[1] = 2 = row = [1, 2, 1]



                # row[1] = [1, 3, 3 , 1 ]



            result.append(rows) # after every loop, we woudl append this here 

            # right now result only has = [1] 

            # for the secon time it will only have [1, 1] 

            # the last thing that result was holding was [1,1]


            # result = [[1], [1,1]]
        return result[rowIndex]

