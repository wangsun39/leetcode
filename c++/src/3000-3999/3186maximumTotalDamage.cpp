#include "lc_pub.h"


class Solution {
    public:
    long long maximumTotalDamage(vector<int>& power) {
        unordered_map<int,int>counter;
        vector<pair<int, int>> p;
        for (auto x: power) {
            counter[x] += 1;
        }
        for (auto &[k,v]: counter) {
            p.push_back({k, v});
        }
        ranges::sort(p);
        int n=p.size();
        vector<long long> dp(n, 0);
        long long ans=dp[0] = (long long)p[0].first * p[0].second;
        long long mx_2=0;
        for (int i=1;i<n;i++) {
            auto [k, v]=p[i];
            dp[i]=(long long)k*v;
            if (p[i].first-p[i-1].first>2)
                dp[i]+=dp[i-1];
            if (i>1&&p[i].first-p[i-2].first>2)
                dp[i]=max(dp[i],dp[i-2]+(long long)k*v);
            if (i>2) {
                mx_2=max(mx_2,dp[i-3]);
                dp[i]=max(dp[i],mx_2+(long long)k*v);
            }
            ans=max(ans,dp[i]);
        }
        return ans;
    }
};

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{2,1,4,3,1,1,1,5};

    Solution so;
    cout << so.maximumTotalDamage(nums) << endl;
    return 0;
}
