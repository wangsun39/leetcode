#include "lc_pub.h"


class Solution {
    public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n=prices.size();
        vector<long long> s1(n + 1, 0), s2(n + 1, 0);
        for (int i=0;i<n;i++) {
            s1[i+1]=s1[i]+prices[i];
            s2[i+1]=s2[i]+prices[i]*strategy[i];
        }
        long long s=s2[n],ans=s2[n];
        for (int i=0;i<n-k+1;i++) {
            long long v=s-(s2[i+k]-s2[i])+s1[i+k]-s1[i+k/2];
            ans=max(ans,v);
        }
        return ans;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[1,1]]");

    Solution so;
    return 0;
}
