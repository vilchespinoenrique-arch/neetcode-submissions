class Solution {
public:
  
  void backtrack(vector<int>& nums, int target, vector<int>& subset, vector<vector<int>>& result, int start){
if(target == 0){

result.push_back(subset);
return;
}

for(int i = start; i < nums.size(); i++){

if(target < nums[i]) continue; // if the nums is bigger than target, then that would mean to ignore that target and continune with something else


subset.push_back(nums[i]);


backtrack(nums, target - nums[i], subset, result, i); // we have to make sure that the target is changing so that we can compare it with the other recursions. 
// we alos want to make sure that the i is not changing unless we have move through recursion.

subset.pop_back();

}

}
  
  
  
  
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {

        vector<int> subset;
        vector<vector<int>> result;

        backtrack(nums, target, subset, result, 0);

        return result;
        
    }
};
