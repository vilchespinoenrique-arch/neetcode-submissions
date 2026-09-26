# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        

        # this quesiton is faily easy, the only hard part of it is to understand it. 

        # the problem is saying that we will get either, 

        # 0, -1, or 1, and depending on what we get, it defines the different things. so if we get:: 

        # a 0 it measn that the num == pick 

        # if we get a - 1 it means that  num> pcik 

        # 1 , my guess is lower.. evenetually we will be able to get to the right answer using binary search. that is the whole idea behind this question 



        left = 0

        right = n 


        while left <= right: 

            mid = (left + right) // 2
            

            result = guess(mid) # the number we will put there will be the middle one, that way we can now where to go 


            if result == 0: 

               return mid # becasue we have found the value 

            elif result == -1: 

                right = mid - 1 

            else: 

                left = mid + 1
                
                 