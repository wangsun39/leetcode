#include "lc_pub.h"

class Solution {
    public:
    long long distributeCandies(int n, int limit) {
        long long  mn1=max(0, n - 2 * limit);
        long long  mx1=min(n,limit);
        if (mn1>mx1) return 0;
        long long ans=0;
        for (int x1=mn1;x1<=mx1;x1++) {
            long long  mn2=max((long long)0,(long long)n-x1-limit);
            long long  mx2=min((long long)n-x1,(long long)limit);
            if (mn2<=mx2)
                ans+=mx2-mn2+1;
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums1{3,2,0,1,0};
    vector<int> nums2{6,5,0};

    Solution so;
    cout << so.distributeCandies(3, 3) << endl;
    return 0;
}
