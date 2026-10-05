class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        


        # look how in each question if we divide by 26, we are able to get the first letter 



        result = ""

        while  columnNumber > 0:
            
            columnNumber -= 1 


            remainder = columnNumber % 26

            result = chr(65 + remainder) + result 


            columnNumber = columnNumber // 26

        # now that number will be the division of what we need 

        return result

    






