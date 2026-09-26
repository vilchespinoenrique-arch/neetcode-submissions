class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        # the question seems a litle confusing at first, but what they want me to do is we will have


        
        # nums 1, once we find the first index of nums1 we will find for it in nums2, once we find it we will to to the right, and then try to find a bigger number, if we do we will 

        # put it in the list, if not we will return -1 



        result = []

         

        for i in range(len(nums1)): 

            if nums1[i] in nums2: # if we find the number inside of nums2... then we will  

                j = nums2.index(nums1[i])  

                # i didnt know about index at all. but if we put a value inside of that index. it will go through the list and it will look for where that values is and it will return the index 


                flag = False

                for k in range(j, (len(nums2) - 1)): 

                    if nums2[j] < nums2[k + 1]: 

                        result.append(nums2[k + 1])

                        flag = True 

                        break 

                    else: 
                        
                        continue 

                
                
                if flag == False: 

                    result.append(-1)


               
        
        return result 
            
        