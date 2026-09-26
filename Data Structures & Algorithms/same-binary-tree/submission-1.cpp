/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

if(!p && !q) return true; // this will mean both are null, so true
if(!p || !q) return false; // this will mean that p or q are null and the other isnt so it would be false
 if(p -> val != q -> val) return false;


 return isSameTree(q -> left, p -> left)  && isSameTree(q-> right, p -> right);      
    }
};
