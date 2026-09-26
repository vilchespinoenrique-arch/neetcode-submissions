class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        

        # for this question we can apply a mathematical formula. 

        # if we have 100 numbers and we want to find the add on of every number 

        # some really cool thing we can do is, we can find a patter and then multiply * 50

        # just look at this 


        # 1 + 100 = 101 

        # 2 + 99 = 101 

        # 3 + 98 = 101 


        # and so on and on. you can do this 50 times, and have 50 pairs that all have the same value 

        # which would be 101 


        # for that we can do 50 * 101 = 5050 


        # and this is our asnwer 


        # we didnt have to add all of the numbers, we found a shortcut for it 

        total = 0



        hashmap = {}
        
        
        for num in nums: 
            

            hashmap[num] = hashmap.get(num, 0) + 1


        # noe we need to calculate every other value.. so if we have for example 3 for for 1. we need to find 

        # the different possible pairs that it has 

        for value in hashmap.values(): 


            new_value = value * (value - 1) // 2

            total = total + new_value 


        return total


