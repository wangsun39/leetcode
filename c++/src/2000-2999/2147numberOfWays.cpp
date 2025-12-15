#include "lc_pub.h"

class Solution {
    public:
    int numberOfWays(string corridor) {
        int MOD=1e9+7;
        vector<int>p;
        int n=corridor.size();
        for (int i=0;i<n;i++) {
            if (corridor[i]=='S')
                p.push_back(i);
        }
        if ((p.size()&1)||p.size()==0) return 0;
        long long ans=1;
        for (int i=2;i<p.size();i+=2) {
            ans *= p[i]-p[i-1];
            ans%=MOD;
        }
        return ans;
    }
    };

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr{1,-3,4};

    Solution so;
    cout << so.numberOfWays("SSPPSPS") << endl;
    return 0;
}
