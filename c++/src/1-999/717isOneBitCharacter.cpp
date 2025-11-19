#include "lc_pub.h"

using namespace std;

class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int n=bits.size();
        vector<int> dp1(n, 0);  // 是否前i位能满足一种组合，且最后是一个字符
        vector<int> dp2(n, 0);  // 是否前i位能满足一种组合，且最后是2个字符
        if (bits[0]==0) dp1[0]=1;
        else if (n>1) {
            dp2[1]=1;
        }
        for (int i=1;i<n;i++) {
            if (dp1[i-1]||dp2[i-1]) {
                if (bits[i]==0) dp1[i]=1;
                else if (i+1<n) {
                    dp2[i+1]=1;
                }
            }
        }
        return dp1[n-1]==1&&dp2[n-1]==0;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays{8,1,6,6};
    Solution so;
    return 0;
}