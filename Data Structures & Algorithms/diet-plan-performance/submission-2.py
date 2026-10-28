class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        

        t = 0 

        

        for j in range(0, len(calories) - k + 1): # so that i can understand, let use the example 

            i = j 

        #  calories = [2,4,1,5] 

        # so len = 4 

        # k = 2 

        # so the range looks like this 

        # (0, 3)

        # lets see if that makes sense 


        # -------- 0 -------

        # i = 0

        # k = 2 

        # j = 0


        # while loop will be 0 < 2



        # ------------ 1 ------- 

        #  i = 1 

        # k = 2 

        # j = 1 


        # while = 1 < 3 


        # ------------- 2 ----------# 

        
        # i = 2

        # k = 2 

        # j = 2

        # while 2 < 4 
            total_sum = 0 


            while i < k + j: 

                total_sum = total_sum + calories[i]

                i += 1

            
            if total_sum < lower:

                t -= 1 

            if total_sum > upper: 

                t += 1 
            
        

        
        return t 


                
