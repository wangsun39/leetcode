#include "lc_pub.h"


class Solution {
    private:
    vector<long long> shortestPathDijkstra(int n, vector<vector<int>>& edges, int start) {
        // 注：如果节点编号从 1 开始（而不是从 0 开始），可以把 n 加一
        vector<vector<pair<int, int>>> g(n); // 邻接表
        for (auto& e : edges) {
            int x = e[0], y = e[1], wt = e[2];
            g[x].emplace_back(y, wt);
            // g[y].emplace_back(x, wt); // 无向图加上这行
        }

        vector<long long> dis(n, LLONG_MAX);
        // 堆中保存 (起点到节点 x 的最短路长度，节点 x)
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
        dis[start] = 0; // 起点到自己的距离是 0
        pq.emplace(0, start);

        while (!pq.empty()) {
            auto [dis_x, x] = pq.top();
            pq.pop();
            if (dis_x > dis[x]) { // x 之前出堆过
                continue;
            }
            for (auto& [y, wt] : g[x]) {
                auto new_dis_y = dis_x + wt;
                if (new_dis_y < dis[y]) {
                    dis[y] = new_dis_y; // 更新 x 的邻居的最短路
                    // 懒更新堆：只插入数据，不更新堆中数据
                    // 相同节点可能有多个不同的 new_dis_y，除了最小的 new_dis_y，其余值都会触发上面的 continue
                    pq.emplace(new_dis_y, y);
                }
            }
        }

        return dis;
    }
    public:
    int minCost(int n, vector<vector<int>>& edges) {
        vector<vector<int>> edges2 = edges;
        for (auto & e: edges) {
            edges2.push_back({e[1],e[0],e[2]*2});
        }
        auto dis=shortestPathDijkstra(n,edges2,0);
        if (dis[n-1]==LLONG_MAX) return -1;
        return dis[n-1];
    }
    };

    
int main()
{
    cout<<"test let us start! %s" << __cplusplus <<std::endl;
    vector<vector<int>>q= parseGrid("[[0,0],[1,0],[0,1],[1,1]]");

    Solution so;
    return 0;
}
