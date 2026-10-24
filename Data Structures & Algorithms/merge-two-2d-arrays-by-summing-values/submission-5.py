class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pass


        # for this question i would like to use 2 pointer and check for the id first and if they match add their values 


        result = []


        i = 0 

        j = 0 

        new_value = 0 


        # the key thing here is that the inputs are order from smaller to bigg

 
        while i < len(nums1) and j < len(nums2):

            if nums1[i][0] == nums2[j][0]:

                new_value = nums1[i][1] + nums2[j][1]

                result.append([nums1[i][0], new_value])

                i += 1

                j += 1 


            elif nums1[i][0] < nums2[j][0]: # if the nums1 is the smaller one, then we want to keep append that value, becaue there is no way that later down the line it could find an id that is that same value, becasue we are going in ascending order 

                result.append([nums1[i][0], nums1[i][1]])

                i += 1 

            else: # so this is the same idea, if nums1 is bigger then we would keep nums2, since there is no possible way that could get a match we appende and we move on 

                result.append([nums2[j][0], nums2[j][1]])

                j += 1 


        result.extend(nums1[i:])

        result.extend(nums2[j:])


     


        return result 