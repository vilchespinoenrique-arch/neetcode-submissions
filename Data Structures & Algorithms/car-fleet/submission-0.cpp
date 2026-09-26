class Solution {
public:
   int carFleet(int target, vector<int>& position, vector<int>& speed) {
    int n = position.size();
    vector<pair<int, double>> cars;  // (position, time to reach destination)
    
    // Calculate time to reach the target for each car and store it
    for (int i = 0; i < n; i++) {
        double time = (double)(target - position[i]) / speed[i];
        cars.push_back({position[i], time});
    }
    
    // Sort cars based on position in descending order (rightmost car first)
    sort(cars.rbegin(), cars.rend());
    
    stack<double> st;  // Stack to keep track of fleet times
    
    for (auto& car : cars) {
        double time = car.second;
        
        // If the stack is empty or the current car's time is greater than the top of stack,
        // this car forms a new fleet.
        if (st.empty() || time > st.top()) {
            st.push(time);
        }
        // Otherwise, the car catches up with the fleet in front and moves at the same pace.
    }
    
    return st.size();  // The number of fleets is the size of the stack
}
};
