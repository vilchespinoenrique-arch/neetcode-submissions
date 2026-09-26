# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # this quesiton has 3 steps 


        # 1) find the midlle 

        # 2) reverse starting from the middle 


        # 3) compare the middle part to the right, with the start 



        slow = head

        fast = head  # have both slow and fast, start in the same part, which will be the head 


        while fast and fast.next: # this is a safety method, but it should be just fine with while fast 

            fast = fast.next.next # fast whille move twice as fast 
            slow = slow.next 

        
        # now slow is the middle part 


        # reverse the linked list starting from the middle 


        current = slow

        prev = None # previous values is now the middle of the linked list 

        while current: 

            current_next = current.next 

            # current_next is a method to save that current next, becasue we are about to use it 

            current.next = prev 

            # so right now our current is poiting to that None 

            # lets visualize this, we have 

            # 3 -> 2 -> 1 

            # and now we say that 

            # 3 -> none # we are saying that 3 should be pointing to none


            prev = current 

            # now our previous, that is None 

            # will become the current that we just modifed 

            # prev = 3 -> none 

            current = current_next

            # current is now 2 


            # so the same process again,

            # we save the next, which is 1 

            # we connect the current that we have to the prev 

            # 2 -> 3 -> none, this is what current is connected to know 


            # and next, we make them prev 

            # prev = 2 -> 3 -> none 

            # and then you just keep on doing that 



            # 3) compare the reversed with the start 

        left = head 

        right = prev 


        while right: 

            if left.val != right.val:
                return False 

            else: 

                left = left.next
                right = right.next 

        return True 