# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        

        current = head 

        i = 0 

         
       

        while current and current.next: 

            
            if i < m - 1 and current.next:

                current = current.next
                
                i += 1 

            elif i == m - 1: 

                i = 0 

                count = 0 
                
                runner = current 

                while count < n and runner.next: 

                    runner = runner.next 

                    count += 1 

                current.next = runner.next 

                current = runner.next 


        return head 
        
