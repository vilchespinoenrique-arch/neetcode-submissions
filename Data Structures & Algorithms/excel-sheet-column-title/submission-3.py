class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        


        # look how in each question if we divide by 26, we are able to get the first letter 


        result = ""


        while columnNumber > 0: 

            # so while that number is still has something to add we will keep going 

            columnNumber = columnNumber - 1 


            r = columnNumber % 26 # here we will get the reaminer of whatever the number is 


            result = chr(65 + r) + result


            columnNumber = columnNumber // 26

        
        
        return result





