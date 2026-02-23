#include "lc_pub.h"

unordered_set<long long> sp2;

class Solution {
    public:
    int binaryGap(int n) {
        int pre=-1,i=0,ans=0;
        while (n) {
            if (n & 1) {
                if (pre != -1) ans=max(ans, i-pre);
                pre = i;
            }
            n>>=1;
            i++;
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