class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        

        # okay so math just broke my brain and made me realize soemthing

        # think of this problem like this 

        # we have [5, 7, 11, 13] 


        # as you can see we are moving from: 

        # 5 -> 7, 7 -> 9, 9 -> 11, 11 -> 13. 

        # as you can see from this example we have 4 movements. 


         # so if we are able to know the amount of moments and the difference between the bigges and the smalles number we will be able to get the amount that is supposed to be in between 

         # we will know this becasue if we know the differenc and we divided that from the steps we got then we will get the number in between each step, basic math 


        difference = arr[-1] - arr[0]

        # this will give us the difference. 

        total_movements = len(arr) 


        # movement from one to another 

        movement_from_one_to_anoter = difference // total_movements


        # the movemment from one to another will give us the moment each on should have so we will be abel to catch the wrong one 

        expected = arr[0]

        for val in arr: 

            if val != expected: 

                return expected

            else: 

                expected += movement_from_one_to_anoter

        
        return val
