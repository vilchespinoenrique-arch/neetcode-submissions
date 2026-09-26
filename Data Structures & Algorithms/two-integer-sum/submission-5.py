class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # for this quesiton we can do something really cool. we can use a hashmap. 


        # if we use a hashmap we can set the key : value idea in order to find our target 


        # so lets look an example 

        # [3, 4, 5, 6]


        # now we can take that first number being the 3 


        # and if we do 3 - 7 = 4. now we know that if we find that 4 or that we have found it in the hashmap then we can go ahead and bring it over. this way we only go throught the array once. and i think that idea is pretty cool 



        hashmap = {} 

        n = len(nums)


        for i in range(0, n): 

            x = target - nums[i]

            if x in hashmap: 

                return [ hashmap[x], i] 

            else: 

                hashmap[nums[i]] = i 
            