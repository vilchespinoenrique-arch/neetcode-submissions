class Solution:
    def countOdds(self, low: int, high: int) -> int:
        

        # for this quesiton what im thinking is to use the low as the start of the for loop and the hight as the end, and then we just go in the for loop, and then we do the remainder thing to get the odd number 

    #    result = []

     #   for i in range(low, high + 1): 
            
#
 #           if i % 2 != 0: 
#
  #              result.append(i)



   #     return len(result)



# now that we dont that this didnt work there is something else we can do. i mean if we really think about what is the example 2, 9. there are 8 number between them. and think about it, if we know how many total number there will be, at least have of those will be odds. however there is a catch
 

 # if we have a number that start odd and finishi odd, it wont half. it will actually be a litlle bit more 


 # 3 - 7  - this will have 5 half, however becasue both are odds, then it comes as 3 total odds. eventhough have is 2.5. so juss something to keep in mind 


 # now lets look at all even 

 # 2 - 8 - 7 numbers total, however, the asnwer is 3 odds only. 



 # now what if it start odds and finishes even or starts even and finishes odds 

 # 4 - 7 - 4 numbers and 2 are odd. 


 # so as a general rule every number will divided by 2 except the numbers that are start and finish with odds 




        total_number = high - low + 1 


        if high % 2 != 0 and low % 2 != 0: 

            return (total_number // 2) + 1

        else: 

            return total_number // 2
