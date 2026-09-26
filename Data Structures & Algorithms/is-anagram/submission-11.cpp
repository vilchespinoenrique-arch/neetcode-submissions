class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false; // If lengths are different, they can't be anagrams
        }

        vector<int> count(26, 0); // Assuming lowercase English letters

        // Count the frequency of each character in string s
        for (char c : s) {
            count[c - 'a']++;
        }

        // Decrease the frequency based on characters in string t
        for (char c : t) {
            count[c - 'a']--;
        }

        // If all counts are zero, the strings are anagrams
        for (int i : count) {
            if (i != 0) {
                return false;
            }
        }

        return true; // All characters matched, so it's an anagram
    }
};
