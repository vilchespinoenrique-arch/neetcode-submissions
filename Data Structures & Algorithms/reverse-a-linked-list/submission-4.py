# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head 


        prev = None 



        while current: 


            next_node = current.next 


            current.next = prev 

            # so right here we attach the current one that we are using to the null, because is inverted so we would do the same thing before. 


            prev = current 

            # now we save that in current, so that we can keep doing it. 

            current = next_node 



        return prev 

        