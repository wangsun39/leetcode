#include "lc_pub.h"

class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        unordered_map<int, int> pre;
        set<int> pos;
        int n = rains.size();
        vector<int> ans(n, -1);
        for (int i=0;i<n;i++) {
            if (rains[i]) {
                if (pre.find(rains[i])==pre.end()) {
                    
                }
                else {
                    auto it=pos.lower_bound(pre[rains[i]]);
                    if (it == pos.end()) return {};
                    ans[*it] = rains[i];
                    pos.erase(*it);
                }
                pre[rains[i]] = i;
            }
            else {
                pos.insert(i);
            }
        }
        for (auto i: pos) ans[i] = 1;
        return ans;
    }
};
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,0,2,0,3,0,2,0,0,0,1,2,3};

    Solution so;
    cout << so.avoidFlood(arr) << endl;
    return 0;
}
