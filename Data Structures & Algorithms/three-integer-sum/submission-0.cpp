

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end()); // Sort the array

        for (int set = 0; set < nums.size() - 2; set++) { // Fix first number
            if (set > 0 && nums[set] == nums[set - 1]) continue; // Skip duplicates

            int left = set + 1, right = nums.size() - 1;

            while (left < right) {
                int sum = nums[set] + nums[left] + nums[right];

                if (sum == 0) {
                    result.push_back({nums[set], nums[left], nums[right]});

                    // Move `left` and `right` to avoid duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } 
                else if (sum < 0) {
                    left++;  // Increase sum
                } 
                else {
                    right--; // Decrease sum
                }
            }
        }
        return result;
    }
};
