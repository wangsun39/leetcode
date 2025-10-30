#include "lc_pub.h"


class Solution {
    
    public:
    int minNumberOperations(vector<int>& target) {
        int n=target.size(),ans=target[0];
        for (int i=0;i<n-1;i++) {
            ans+=max(target[i+1]-target[i],0);
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
