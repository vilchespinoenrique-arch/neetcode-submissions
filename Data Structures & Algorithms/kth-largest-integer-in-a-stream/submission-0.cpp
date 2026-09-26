class KthLargest {

private:

priority_queue<int, vector<int> , greater<int>> minheap; 
// here priority_queue this is how you create a minheap, you have to start it as priority_ queue. 
// the int is because we are going to be using int, and the vector int is going to be the group of integers that we are going to use to create the heap,
// the greater<int> is what makes sure that this become a min heap, if we dont add this part this will become a max heap.
int k; // we need to declare the variable k here. 

public:

KthLargest(int k, vector <int>& nums){  // this is our constructor 

  this -> k = k; // this is assigning the value oif the parameter k to the member vaiable k of the object. this ensures that the object has it own version of km whcih can be accesses later in the class methods

  for(int num : nums){ // this is taking the numbers from the vector and is going using them as int num, and doing something with them, whcih we dont know what it is yet.

    minheap.push(num); // this is going to put the numbers inside the heap.

  if(minheap.size() > k){ // if the size of the heap is bigger than k, then it will mean that we are going to pop the last element. which would be the smalles element. 

    minheap.pop();
  }


}
}


int add(int val){
  minheap.push(val); // this will add a new value to the heap.

  if(minheap.size() > k){
minheap.pop(); // if the minheap size is bigger we also pop over here the smalles element.

    
  }
  return minheap.top();
}
};