#include "lc_pub.h"

class Solution {
    public:
    int minOperations(vector<int>& nums) {
        int g=nums[0], n=nums.size(),c1=0;
        for (auto x: nums) {
            g=gcd(g, x);
            if (x==1) c1++;
        }
        if (g > 1) return -1;
        if (c1) return n-c1;
        vector<pair<int, int>> g1;
        int mn=n;  // 最小能合并成1的子区间长度

        for (int i=0;i<n;i++) {
            int x=nums[i];
            for (int j=g1.size()-1;j>=0;j--) {
                g1[j].first=gcd(g1[j].first, x);
            }
            g1.push_back({x, i});
            // g1 去重
            int cur=0;
            for (int j=0;j<g1.size();j++) {
                if (g1[cur].first==g1[j].first) {
                    g1[cur]=g1[j];
                }
                else {
                    cur++;
                    g1[cur]=g1[j];
                }
                if (g1[cur].first==1) mn=min(mn, i-g1[cur].second+1);
            }
            g1.resize(cur+1);
        }
        return mn-1+n-1;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {2,6,3,4};

    Solution so;
    cout << so.minOperations(arr) << endl;
    return 0;
}
