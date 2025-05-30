#include "lc_pub.h"


class Solution {
    public:
    int closestMeetingNode(vector<int>& edges, int node1, int node2) {
        int n = edges.size() + 1;
        unordered_map<int, int> mp1,mp2;
        int cur = node1;
        int cnt=0;
        while (cur!=-1&&mp1.find(cur)==mp1.end()) {
            mp1[cur]=cnt++;
            cur = edges[cur];
        }
        cur = node2;
        cnt=0;
        while (cur!=-1&&mp2.find(cur)==mp2.end()) {
            mp2[cur]=cnt++;
            cur = edges[cur];
        }
        int ans = n;
        int mx = n;
        for (auto& [k, v]: mp1) {
            if (mp2.find(k) == mp2.end()) continue;
            if(mx > max(v, mp2[k])) {
                mx = max(v, mp2[k]);
                ans = k;
            }
            else if (mx==max(v, mp2[k])) {
                ans = min(ans,k);
            }
        }
        if (ans == n) return -1;
        return ans;
    }
    };
    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {2,2,3,-1};

    Solution so;
    cout << so.closestMeetingNode(arr,0,1) << endl;
    return 0;
}
