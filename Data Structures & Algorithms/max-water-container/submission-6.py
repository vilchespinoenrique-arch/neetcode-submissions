class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0 
        right = len(heights) - 1  

        # set up the two pointers 

        # [1,7, 2, 5, 4, 7, 3, 6]

        holding_the_possible_values = []

        while left < right: 

            holding_water = min(heights[left], heights[right]) * (right - left)

            # we will be holding the water in this variable. 

            if not holding_the_possible_values or holding_the_possible_values[-1] < holding_water: 
                holding_the_possible_values.append(holding_water)

            
            if heights[left] < heights[right]:
                left = left + 1

            else: 
                right = right - 1 


        # my main question with this problem is if we have two values that are the same, in that case, we would move with each one, becasue depending on whihc one we move, it means that we could change the result 

        # [1 ,7, 2, 5, 4, 1, 3, 1]  # for example here, if we have this, and lets say we move the right side if we do that, that would mean that we get

        # 6 * 3, and then 6 * 1.. and so on and on/ we would never get the combination of 6 * 7 if we were to move the pointer of the left side. 

        # the reason why it doesnt matter, is becasue we would end up getting the best combination no matter what 
        
        # becasue even if we did 6 and 7.. it wouldnt really matter, becasue the multiplcation would be min between this two, which i cant of completely went past this,
        # if this is this case, that means that the it doesnt matter where you go, becasue you will have the min regardles 

        # the math is pretty hard, but see it with the exaple, you can notice, that it doesnt matter to which side you go, you will not get a better answer momentarily thant that one.. is just a width thing, and you have to consider 
        # that no matter what in the next example you will use the min, so even if the numbers of the side where bigger, it would never be bigger than the one before, becasue it will take the min and calculate, the width in the best of cases will remain same, and in the worst of cases it will go down.. it cannot go more than the current width is imposible, becasue both are equal 

        # deeply think about that last line 





        return holding_the_possible_values[-1] if holding_the_possible_values else 0 