#include "lc_pub.h"

class Solution {
    public:
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        int MOD=1e9+7;
        unordered_set<int>rows;
        hFences.push_back(1);
        hFences.push_back(m);
        vFences.push_back(1);
        vFences.push_back(n);
        for (int i=0;i<hFences.size();i++) {
            for (int j=0;j<hFences.size();j++) {
                rows.insert(abs(hFences[i]-hFences[j]));
            }
        }
        long long ans = 0;
        for (int i=0;i<vFences.size();i++) {
            for (int j=0;j<vFences.size();j++) {
                int v = abs(vFences[i]-vFences[j]);
                if (rows.find(v) == rows.end()) continue;
                ans = max(ans, (long long)v*v);
            }
        }
        if (ans==0) return -1;
        return ans%MOD;
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> nums{2,3},nums2{2};

    Solution so;
    cout << so.maximizeSquareArea(4, 3, nums, nums2) << endl;
    return 0;
}
