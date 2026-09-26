class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        

        # there is a clever way to do this, and for that we need to understand that the way we will replace a number is if: 



        # the left element is 0, or we are at the start, which would make it 0 as well 



        # the right side is also at the end and is also 0 


        count = 0


        for i in range(len(flowerbed)):

            left_side = (i == 0) or (flowerbed[i - 1] == 0) 


            right_side = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0) 



            if flowerbed[i] == 0 and left_side and right_side: 

                flowerbed[i] = 1
                count += 1


        
        if count >= n: 

            return True

        else: 
            return False 