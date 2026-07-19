

#include "lc_pub.h"

class Solution {
public:
    long long maximumValue(int n, int s, int m) {
        int n1=(n)/2,n2=(n-1)/2;
        long long ans=0;
        if (n1>n2||n1==0)
            ans+=s+(long long)n1*m-n2;
        else
            ans+=s+(long long)n1*m-n2+1;
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{0,0,0,2,0};
    auto items=parseGrid("[[2,4],[3,2],[4,1],[6,4],[12,4]]");

    Solution so;
    return 0;
}
