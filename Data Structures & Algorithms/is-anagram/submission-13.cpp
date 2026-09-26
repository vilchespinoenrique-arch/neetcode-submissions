class Solution {
public:
    bool isAnagram(string s, string t) {

      if(s.length() != t.length()){
        return false;
      }

int HoldAlphaber[26] = {0}; 

   for (char c : s){
     HoldAlphaber[c - 'a']++; 
     
       }

      for (char c : t){
         HoldAlphaber[c - 'a']--;
}
for(int i = 0; i < 26; i++){
  if(HoldAlphaber[i] != 0){
    return false;
  }
}
      return true;

    }   
      

};