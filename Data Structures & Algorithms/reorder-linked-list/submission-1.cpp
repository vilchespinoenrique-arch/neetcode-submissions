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
    void reorderList(ListNode* head) {

        if(!head || !head -> next) return; // this means that if we have an empty linked list or just 1 in the linked list, it means that we will go back
        
ListNode* slow = head; // we make the slow pointer move 1 at a time
ListNode* fast = head; // we make the fast pointer move 2 at a time

while(fast -> next && fast -> next -> next){ // this makes a while loop using a fast pointer instead of a while loop

slow = slow -> next;
fast = fast -> next -> next;
}

// this is setting the slow pointer to point to the middle.

// now we want to reverse the list, but the upper half

ListNode* current = slow -> next; // we set it as slow next, becasue we want to start 1 more than the middle
ListNode* prev = nullptr;


while(current!= nullptr){
ListNode* next = current -> next; // save the next of current into next, so that we can change later on
current -> next = prev; // we set the next current to be the prev, that will be the last iteration from before
prev = current; // set prev to current;
current = next; // move to the next one.

}

 slow->next = nullptr;  // Split the list into two parts

    // Step 3: Merge two halves
    ListNode* first = head;
    ListNode* second = prev;
    while (second) {
        ListNode* tmp1 = first->next;
        ListNode* tmp2 = second->next;

        first->next = second;
        second->next = tmp1;

        first = tmp1;
        second = tmp2;
    }
}






};
