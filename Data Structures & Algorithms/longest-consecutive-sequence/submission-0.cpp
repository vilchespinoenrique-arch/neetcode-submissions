class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

            unordered_set<int> numSet(nums.begin(), nums.end()); // Convert the vector to an unordered set
        
        int counter = 0; // This will keep track of the length of the longest sequence
        
        for(int num : nums) { // Iterate through each number in the original array
            // Check if num - 1 is not in the set, meaning num is the start of a new sequence
            if(numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentSeq = 1; // Start a sequence with this number
                
                // Look for consecutive numbers starting from num
                while(numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum++; // Move to the next consecutive number
                    currentSeq++;  // Increase the sequence length
                }
                
                // Update the counter if the current sequence is the longest found so far
                counter = max(counter, currentSeq);
            }
        }
        
        return counter; // Return the length of the longest consecutive sequence
  
        
    }
};
