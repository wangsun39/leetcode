#include "lc_pub.h"

#define ST_GET_KEY 1
#define ST_GET_BOX 2
#define ST_GET_BOTH 3


class Solution {
    
    public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int n = status.size();
        int ans = 0;
        vector<int> vis(n, 0), st(n, 0);
        deque<int> dq;
        for (auto x: initialBoxes) {
            st[x] |= ST_GET_BOX;
            if (!status[x]) continue;
            dq.push_back(x);
            vis[x] = 1;
            st[x] = ST_GET_BOTH;
        }
        while (dq.size()) {
            int x = dq[0];
            ans += candies[x];
            dq.pop_front();
            for (auto y: containedBoxes[x]) {
                if (vis[y]) continue;
                st[y] |= ST_GET_BOX;
                if (st[y] == ST_GET_BOTH || status[y]) {
                    dq.push_back(y);
                    vis[y] = 1;
                }
            }
            for (auto y: keys[x]) {
                if (vis[y]) continue;
                st[y] |= ST_GET_KEY;
                if (st[y] == ST_GET_BOTH) {
                    dq.push_back(y);
                    vis[y] = 1;
                }
            }
        }
        return ans;
    }
};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;

    Solution so;
    return 0;
}
