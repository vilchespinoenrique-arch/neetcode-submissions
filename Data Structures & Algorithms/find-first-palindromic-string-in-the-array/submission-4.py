class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pass



    
        

       
            

        for word in words: 
                

            right = len(word) - 1 

            left = 0

            flag = True  
        

            while left <= right: 
            
                if word[right] != word[left]: 

                    flag = False

                    break 

                
                else: 

                    right -= 1 

                    left += 1 


            if flag == True: 

                return word
        
        return ""


         
        

            

            
            
                


