#include "lc_pub.h"


class Solution {
    public:
    long long flowerGame(int n, int m) {
        long long ans = 0;
        for (int i=1;i<=n;i++) {
            if (i & 1) ans += m/2;
            else ans+=(m+1)/2;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{3,3,3};

    Solution so;
    cout << so.flowerGame(3,2) << endl;
    return 0;
}
