class Solution {
private:

priority_queue<int> maxheap;


public:
    int lastStoneWeight(vector<int>& stones) {

for(int stone : stones){

maxheap.push(stone); // this will arange them so that i can get the biggest value at the top and the smalles values at the end.
}

while(maxheap.size() > 1){


int x = maxheap.top();
maxheap.pop();

int y = maxheap.top();
maxheap.pop();


if(x != y){

maxheap.push(x-y);

} 
}




return maxheap.empty() ? 0 : maxheap.top();

}



        
    
};
