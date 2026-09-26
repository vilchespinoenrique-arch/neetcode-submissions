class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        
         int left = 1, right = *max_element(piles.begin(), piles.end());
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        int hours = 0;
        
        for (int pile : piles) {
            hours += (pile + mid - 1) / mid;  // Compute hours needed at rate `mid`
        }
        
        if (hours > h) {
            left = mid + 1;  // Increase speed if we need more hours than `h`
        } else {
            right = mid;  // Try a lower speed
        }
    }
    
    return left;

    }
};
