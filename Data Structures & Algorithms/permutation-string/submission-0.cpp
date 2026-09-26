class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false; // s1 cannot be a substring of s2 if it's longer
        
        vector<int> s1Freq(26, 0), windowFreq(26, 0);
        
        // Count character frequencies in s1
        for (char c : s1) {
            s1Freq[c - 'a']++;
        }

        int left = 0, right = 0;
        
        // Expand window to the size of s1
        while (right < s2.length()) {
            windowFreq[s2[right] - 'a']++; // Add right character to window
            
            // If window is larger than s1, remove leftmost character
            if (right - left + 1 > s1.length()) {
                windowFreq[s2[left] - 'a']--;
                left++;  // Move left pointer forward
            }
            
            // Check if window matches s1 frequency
            if (s1Freq == windowFreq) {
                return true;
            }
            
            right++;  // Expand right pointer
        }
        
        return false;
    }
};