#include <iostream>
#include <map>
#include <string>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //some empty data structure i think map???
        //parse through entire vector nums and if its IN maps return false
        //if its NOT in maps then add it urself, this is the key btw 
        std::map<int, std::string> values; //a map with the NUMS as the keys and the same "Exists" string as valuues

        for (const auto& num : nums) {
            if(values.count(num)){
                return true; 
            }else{
                values.insert({num, "Exists"}); 
            }
        }
        return false; 
    }
};