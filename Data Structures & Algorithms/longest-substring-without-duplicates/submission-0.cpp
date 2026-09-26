class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;  // Set to keep track of unique characters in the window
        int left = 0;  // Left pointer of the window
        int maxLength = 0;  // Maximum length of substring without repeating characters
        
        // Iterate over the string with the right pointer
        for (int right = 0; right < s.length(); ++right) {
            // If character at 'right' is already in the set, move 'left' pointer
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);  // Remove character at 'left' from the set
                left++;  // Move 'left' to the right
            }
            charSet.insert(s[right]);  // Add character at 'right' to the set
            maxLength = max(maxLength, right - left + 1);  // Update maxLength
        }
        
        return maxLength;  // Return the result
    }
};
