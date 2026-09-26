class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {
            // Skip non-alphanumeric characters
            while (l < r && !isalnum(s[l])) l++;
            while (l < r && !isalnum(s[r])) r--;

            // Compare characters case-insensitively
            if (tolower(s[l]) != tolower(s[r])) {
                return false;
            }

            // Move pointers inward
            l++;
            r--;
        }

        return true;  // If we finish the loop, it's a palindrome
    }
};