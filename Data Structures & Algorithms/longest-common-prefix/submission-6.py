class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        # longest common prefix is good to answer it using divide and conquer approach

        
        if len(strs) == 1:
            return strs[0] # once we only have one value go ahead and return it 

        mid = len(strs)//2 

        
        left = self.longestCommonPrefix(strs[:mid]) # tne left side of the mid 
        right = self.longestCommonPrefix(strs[mid:]) # the righ side of the mide 


        return self.longes_common(left,right)



    def longes_common(self,strs1, strs2):

        result = ""

        for i in range(min(len(strs1),len(strs2))):
            if strs1[i] == strs2[i]:
                result = result + strs1[i]
            else: 
                break 

            
        return result
