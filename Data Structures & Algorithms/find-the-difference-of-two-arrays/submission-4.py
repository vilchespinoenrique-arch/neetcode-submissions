class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        

        # this question has something that comes froms sets, which i had no idea that were a thing. this is that if you comapre 2 sets from 2 different list they are multiple things you can do. one of them is taking out the ones that are the same with each other. 


        new_set1 = set(nums1)


        new_set2 = set(nums2)



        # now we have 2 sets, and like i said there are multiple things you can do with sets 


        return [list(new_set1 - new_set2), list(new_set2 - new_set1)]
       


        return new_list1

            

