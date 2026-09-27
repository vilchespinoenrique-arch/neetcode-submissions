class Solution:
    def maxScore(self, s: str) -> int:
        

        count_zeroes = 0 

        total_ones = s.count('1') 

        best = 0

        for i in range(len(s) - 1):

            if s[i] == '0': 

                count_zeroes += 1 

            elif s[i] == '1': 

                total_ones -= 1 

            best = max(best, count_zeroes + total_ones)

        
        return best 
            
