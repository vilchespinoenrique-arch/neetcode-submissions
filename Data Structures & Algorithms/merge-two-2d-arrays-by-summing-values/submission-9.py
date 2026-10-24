class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pass


        # for this question what we want to do, is we want to see if the ids are equal to each other, and if they are then we just add the value 


        # now there are 2 possible options, the id of nums 1 is bigger, then we would keep the id of nums 2, becasue since is increasing order, the smaller value could never have a match but the bigger value coudl have a macy 


        # the other posibility, is that nums2 is bigger, then in that case becasue of the same logic, we will take the nums1. sice nums 2 has a chance but nusm1 doesnt. 



        new_number = 0 

        i = 0  # will be in charge of nums 1 

        j = 0  # will  be in charge of nums 2


        result = []



        while i < len(nums1) and j < len(nums2):

            
            if nums1[i][0] == nums2[j][0]:
                

                new_number = nums1[i][1] + nums2[j][1]

                result.append([nums1[i][0], new_number])

                i += 1

                j += 1


            elif nums1[i][0] < nums2[j][0]:

                # if nums2 is bigger, then nums 1 has no chance 

                result.append([nums1[i][0], nums1[i][1]])

                i += 1 


            else: 

                result.append([nums2[j][0], nums2[j][1]])

                j += 1 


        result.extend(nums1[i:])


        result.extend(nums2[j:])


        return result 



            
            






