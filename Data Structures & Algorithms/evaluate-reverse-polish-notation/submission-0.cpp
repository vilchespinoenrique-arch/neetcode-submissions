
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;

        for (string c : tokens) {
            if (c == "+") {
                int a = myStack.top(); myStack.pop();
                int b = myStack.top(); myStack.pop();
                myStack.push(b + a);
            } else if (c == "-") {
                int a = myStack.top(); myStack.pop();
                int b = myStack.top(); myStack.pop();
                myStack.push(b - a);
            } else if (c == "*") {
                int a = myStack.top(); myStack.pop();
                int b = myStack.top(); myStack.pop();
                myStack.push(b * a);
            } else if (c == "/") {
                int a = myStack.top(); myStack.pop();
                int b = myStack.top(); myStack.pop();
                myStack.push(b / a);
            } else { 
                myStack.push(stoi(c)); // Convert string to integer and push
            }
        }

        return myStack.top(); // Return the final result after processing all tokens
    }
};