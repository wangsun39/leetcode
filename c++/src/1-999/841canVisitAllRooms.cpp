#include "lc_pub.h"


class Solution {
    public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> vis(n, false);
        vis[0] = true;
        deque<int> dq;
        dq.push_back(0);
        while (dq.size()) {
            int i = dq[0];
            dq.pop_front();
            for (int j: rooms[i]) {
                if (vis[j]) continue;
                dq.push_back(j);
                vis[j] = true;
            }
        }
        return all_of(vis.begin(), vis.end(), [](bool x) {return x;});
    }

};

int main()
{
    std::cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arrays = {1,1,2};
    Solution so;
    return 0;
}