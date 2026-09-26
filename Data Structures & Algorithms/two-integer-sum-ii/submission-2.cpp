class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                return {left + 1, right + 1}; // Convert to 1-based index
            } 
            else if (sum < target) {
                left++; // Move left pointer to increase sum
            } 
            else {
                right--; // Move right pointer to decrease sum
            }
        }

        return {}; // No solution found
    }
};
