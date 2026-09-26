class Solution {
public:
   int search(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());  // Organize in ascending order

    int left = 0;
    int right = nums.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;  // Find middle index

        if (nums[mid] == target) {
            return mid;  // Target found
        } else if (nums[mid] > target) {
            right = mid - 1;  // Search left half
        } else {
            left = mid + 1;  // Search right half
        }
    }

    return -1;  // Target not found
}
};