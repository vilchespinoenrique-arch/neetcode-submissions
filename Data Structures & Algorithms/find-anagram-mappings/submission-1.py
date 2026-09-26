class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        # for this question the first thign i want to do is go throguht nums2 and create my map. it will have the keys as the values

        # and the values as the index 

        # it will look like this 


        # nums2 = {50:0, 12: 1, 32: 2, 46: 3, 28: 4} 


        # then i will go throught nums1, and just look for my numbers, and return their index 



        result = [] 

        hashmap = {} 


        for i in range(len(nums2)): 

            hashmap[nums2[i]] = i 

            # so we will have 


        # hashmap = {50:0, 12: 1, 32: 2, 46: 3, 28: 4}  


        for number in nums1: 

            if number in hashmap: 

                result.append(hashmap[number])


        return result  