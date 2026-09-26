class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> freqMap;
        int left = 0, maxFreq = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            freqMap[s[right]]++;  // Add the character at `right` to the frequency map
            maxFreq = max(maxFreq, freqMap[s[right]]);  // Track the most frequent character count

            // If (window size - maxFreq) > k, shrink the window
            if ((right - left + 1) - maxFreq > k) {
                freqMap[s[left]]--;  // Remove the character at `left` from window
                left++;  // Move `left` pointer
            }

            maxLength = max(maxLength, right - left + 1);  // Update max length
        }

        return maxLength;
    }
};