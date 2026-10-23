class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pass


        # for this question i would like to use 2 pointer and check for the id first and if they match add their values 


        result = []


        i = 0 

        j = 0 

        new_value = 0 

 
        while i < len(nums1) and j < len(nums2): 

            if nums1[i][0] == nums2[j][0]:
                new_value = nums1[i][1] + nums2[j][1]
                result.append([nums1[i][0], new_value])

                i += 1 

                j += 1 

            elif nums1[i][0] < nums2[j][0]:

                result.append([nums1[i][0], nums1[i][1]])

                i += 1 
            else: 

                result.append([nums2[j][0], nums2[j][1]])

                j += 1

        # as for the ones that were left, and where never looked 


        result.extend(nums1[i:])

        result.extend(nums2[j:])

        

        return result 