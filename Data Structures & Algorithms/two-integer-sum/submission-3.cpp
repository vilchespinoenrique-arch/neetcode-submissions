class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

vector<int> result;
  
  for(int i = 0; i < nums.size(); i++){
    for(int j = 1 + i; j < nums.size(); j++){
if(nums[i] + nums[j] == target){
if( i < j){
result.push_back(i); // this will put the i go print out first 
result.push_back(j); // and j second. 
  }else {
  result.push_back(j); 
  result.push_back(i); 
}

return result;


  
  }
  
}

   
  
}

    }
};
