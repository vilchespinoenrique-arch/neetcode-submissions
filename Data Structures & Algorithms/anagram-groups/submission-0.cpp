class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

          // Create a hash map to store sorted string as key and a vector of anagrams as value
        unordered_map<string, vector<string>> anagramMap;
        
        // Iterate over each string in the input vector
        for (const string& str : strs) {
            // Create a copy of the string and sort it
            string sortedStr = str;
            sort(sortedStr.begin(), sortedStr.end());
            
            // Group the original string into the corresponding anagram bucket
            anagramMap[sortedStr].push_back(str);
        }
        
        // Prepare the result vector to return the grouped anagrams
        vector<vector<string>> result;
        
        // Add each group of anagrams to the result vector
        for (const auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        
        return result;
    
        
    }
};
