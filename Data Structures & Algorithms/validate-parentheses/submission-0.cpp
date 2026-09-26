class Solution {
public:
    bool isValid(string s) {

              stack<char> mystack;  // Stack to store open brackets
        map<char, char> myMap = { 
            {')', '('},  
            {']', '['},  
            {'}', '{'}   
        };

        for(char c: s) {  
            if(myMap.count(c)) {  // If 'c' is a closing bracket
                if(mystack.empty() || mystack.top() != myMap[c]) {  
                    return false;  // Mismatch or no opening bracket
                }
                mystack.pop();  // Pop the matched opening bracket
            } else {
                mystack.push(c);  // Push opening bracket onto the stack
            }   
        }
        return mystack.empty();  // If stack is empty, all brackets matched
    
        
    }
};
