/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {

    ListNode* curr = head;
    ListNode* prev = nullptr;

    while(curr){
ListNode* next = curr -> next; // this is going to point to the the 2 of the linked list
curr -> next = prev; // this is going to point to null the curr, which is 1 to point to null.  
prev = curr; // this is going to make so that the prev is now 1. so that when the linked list want to point to the prev, it will always be the current next. 
curr = next; // this is going to make it so that we can deal with the next node.
}

return prev;
        
    }
};
