#include "lc_pub.h"

class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        ranges::sort(events, {}, [](auto &e) {return e[1];});
        int ans=events[0][2];
        vector<pair<int,int>> st;
        st.push_back({events[0][1],events[0][2]});
        int n=events.size();
        for (int i=1;i<n;i++) {
            auto it = ranges::lower_bound(st, events[i][0], {}, [&] (auto &x){return x.first;});
            if (it!=st.begin()) {
                ans = max(ans, (it-1)->second + events[i][2]);
            }
            else {
                ans = max(ans, events[i][2]);
            }
            if (events[i][2] > st.back().second) {
                st.push_back({events[i][1],events[i][2]});
            }
        }
        return ans;
    }
};

int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    auto arr=parseGrid("[[1,3,2],[4,5,2],[2,4,3]]");

    Solution so;
    cout << so.maxTwoEvents(arr) << endl;
    return 0;
}
