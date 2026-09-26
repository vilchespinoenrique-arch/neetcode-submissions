class Solution {
public:
    int maxSubArray(vector<int>& nums) {

int current_sum = nums[0];
int max_value = nums[0];  // we are going to set the first one for both

      // we are going to assume that we have the number [1, 4, -2, 6]

for(int i = 1; i < nums.size(); i++){
current_sum = max(nums[i], current_sum + nums[i]); // so here we are going to be comparing 1, 1 + 1 

  max_value = max(max_value, current_sum); // so whatever here we are going to compare the current sum that we got and the max value

}
  return max_value;
    
    }
};
