class Solution:
    def scoreOfString(self, s: str) -> int:
        
        # something that i  didnt know is that if you use ord.

        # ord caluclates the ASCII value for you 

        # and then absoule value is represented as abs 
        
        total = 0

        for i in range(0, len(s) - 1): 

           diff  = abs(ord(s[i]) - ord(s[i+1])) 

           total += diff 

        return total 

