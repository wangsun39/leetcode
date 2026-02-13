#include "lc_pub.h"


class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map<int,int>c;
        for(int x:nums) c[x]+=1;
        for(auto&[k,v]:c) if(v&1) return false;
        return true;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr = parseGrid("[[3,2],[4,3],[4,4],[2,5]]");
    vector<int> n1{3,4,9,1,3,9,5}, n2{0,1,2,3};

    Solution so;
    return 0;
}
