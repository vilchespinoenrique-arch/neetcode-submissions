class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        

        # for this question what you want to do is you want to add from both sides, and when ever the rows are odds, we would then subtract the number in the middle, so it should be pretty ease 


        total = 0

        row_total = len(mat) # this returns 3 

        column_total = len(mat[0]) # this returs 3 


        i = 0 

        j = 0

        while i < row_total and j < column_total: 

                # from left to right it will look like this 

                total += mat[i][j] 

                i += 1 

                j += 1 

                # so we increase 1 everytime frim left to right 


                
        i =  row_total - 1

        j = 0

        while i >= 0 and j >= 0:
            
            # this will be the left side

            total += mat[i][j]

            i -= 1

            j += 1


        # if the rows are odd we need to subtract the middle one 

        if row_total % 2 == 1: 
            
            total = total - mat[row_total // 2][column_total// 2]


        return total 



        






