class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for this question what you want to do is you want to use a hashmap. and the reason for this is because you want to keep track of what you have seen and match it with the index. if you are able to see a number that satifies the formula i would show it means that we found a match. if you found a mathc it measn the combination of that match is the answer or the possible asnwer 



        hashmap = {}

        length = len(nums)



        for i in range(0, length): 

            x = target - nums[i] 

            # this would be 7 - 3 = 4. so if we find a 4 in the hasmap it measn that we would have a perfect match 


            if x in hashmap: 

                return [hashmap[x], i] # this would return the hashmap index that we found the pair and the i the one that we are currently one 


            else: 

                hashmap[nums[i]] = i # pair the curent number with their index

