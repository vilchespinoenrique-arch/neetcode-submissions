class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        # for this quesiton what you want to do is you want to take the number that has 2 values and put in the list, and then the number that is not showing in the hasmap you also put that one 



        hashmap = {} 



        for num in nums: 


            hashmap[num] = hashmap.get(num , 0) + 1 



        # so now we are going to have this 


        # {1 : 1, 2: 2, 4 : 1}


        new_list = []


        for key, value in hashmap.items():


            if value == 2: 

                new_list.append(key)


        
        for i in range(1, len(nums) + 1): 

            if i not in hashmap: 

                new_list.append(i)



        return new_list









