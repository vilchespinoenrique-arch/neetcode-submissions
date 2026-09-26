class Solution {
public:
    int findMin(vector<int> &nums) {

            int left = 0;
    int right = nums.size() - 1;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        
        // If mid is greater than right, the minimum is in the right half
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else {
            // Otherwise, the minimum is in the left half or at mid
            right = mid;
        }
    }
    
    // When left == right, we found the minimum
    return nums[left];

        
    }
};
