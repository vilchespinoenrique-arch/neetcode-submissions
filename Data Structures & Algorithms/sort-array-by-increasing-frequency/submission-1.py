class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:


        # for this question we want to get the values of each, and who then i want to sorted them by their values, which i would with sorted 


        hashmap = {} 


        for num in nums: 

            hashmap[num] = hashmap.get(num, 0) + 1 



        # now we have a whole list of all the frequencies 


        # so now i want to organize that in increasing order 


        new_hashmap = dict(sorted(hashmap.items(), key=lambda pair: (pair[1], -pair[0]))) 

        # to keep in mind the pair[1] and -pair[0] that second part, becasu of the comma is a second rule in case there is a tie. that is how tupples behave, so it makes it perfect. it will see that they are equal and it will take the biggest number first, becasue we apply that -, and that - makes a number like 19 into a -19 so if its being compared with a 17. it will take the biggest number first making it decreasing order 


        # now the hasmap is organize by the value and it will look like this: 


        # { 3: 1, 1 : 2, 1 : 3}

        new_list = [] 



        for key, value in new_hashmap.items(): 


            for i in range(0, value): 

                new_list.append(key)


        return new_list

        