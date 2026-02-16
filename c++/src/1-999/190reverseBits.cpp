#include "lc_pub.h"

class Solution {
    
    public:
    int reverseBits(int n) {
        int ans=0;
        for (int i=0;i<32;i++) {
            ans = (ans << 1) + (n & 1);
            n >>= 1;
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    cout<< so.reverseBits(3)<<endl;
    return 0;
}
