#include "lc_pub.h"

class Solution {
    static constexpr int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size(), m = moveTime[0].size();
        vector<vector<int>> dis(n, vector<int>(m, INT_MAX));
        dis[0][0] = 0;
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        pq.emplace(0, 0, 0);
        while (true) {
            auto [d, i, j] = pq.top();
            pq.pop();
            if (i == n - 1 && j == m - 1) {
                return d;
            }
            if (d > dis[i][j]) {
                continue;
            }
            int time = (i + j) % 2 + 1;
            for (auto& q : dirs) {
                int x = i + q[0], y = j + q[1];
                if (0 <= x && x < n && 0 <= y && y < m) {
                    int new_dis = max(d, moveTime[x][y]) + time;
                    if (new_dis < dis[x][y]) {
                        dis[x][y] = new_dis;
                        pq.emplace(new_dis, x, y);
                    }
                }
            }
        }
    }
};


    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<int> arr = {1,1,1,2,2};

    Solution so;
    // so.addText("leetcode");
    // cout << so.deleteText(10) << endl;
    return 0;
}
