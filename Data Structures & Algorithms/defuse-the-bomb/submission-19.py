class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        pass


        # for this question the first thing to understand are circular arrays 


        # the way we deal with them is we use a modulus, that way we can circle back to any array. look at this 



        #  [1,2,3], lets say we want pointer 4, which shouldnt really exist, but we can pull it out anyways. 


        # 3 % 3, here we grab, where the pointer should be, which is 3, and the lenght of the array which is 3

        # and this will give us 0. which is 1, which is where poitner 3 would be 



        result = []



        if k == 0: 

            result = [0] * len(code)

            return result 




        for j in range(0, len(code)): 
            

            if k > 0: # if k is bigger than 0, meaning is positive 
                
                i = j + 1

                total_sum = 0

                while i <= k + j: 

                    total_sum = total_sum + code[i % len(code)]


                    i += 1 

                result.append(total_sum)


            else: 
                
                i = j - 1

                total_sum = 0 

                while i >= j + k: 

                    total_sum = total_sum + code[i % len(code)]

                    
                    i -= 1 

                result.append(total_sum)

        
        return result 






            



